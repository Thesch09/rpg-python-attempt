from rich import print

# AIs
from enemy_ai import dummy_AI
from enemy_ai import goblin_AI
from enemy_ai import rock_AI


# Events
from events import do_combat


from moves import Moves
from enemy import Enemy
# from oppgave_6_NPC_module import enemyList
import random
import math
import time


class Player:
    # Create character
    def __init__(self, first_name, surname, max_hp, max_mp, strength, ac, charged, moves, xp, level, shmeckle):
        self.first_name = first_name
        self.surname = surname
        self.max_hp = max_hp
        self.hp = self.max_hp
        self.max_mp = max_mp
        self.mana = self.max_mp
        self.strength = strength
        self.ac = ac
        self.guard = False
        self.charged = charged
        self.moves = moves
        self.xp = xp
        self.level = level
        self.strength_point = 0
        self.xp_til_level_up = 6
        self.tot_xp = 0
        self.shmeckle = shmeckle
        self.lvl_rewards = [multiStab]
        self.lvl_rewards_no = [3]
    
    # Take damage
    def take_damage(self, amount):
        if self.guard == True:
            # Reduced if guarding
            print(f"{self.first_name} will take reduced damage")
            amount -= amount / 3
            amount = math.floor(amount)

        self.hp -= amount
        fatality = ""
        if self.hp < 0:
            self.hp = 0
            fatality = "[red]fatal[/red] "
        print(f"{self.first_name} took {amount} points of {fatality}damage and now has {self.hp} HP!")

    # Check if alive
    def is_alive(self):
        return self.hp > 0
    
    # Target dummy's special move
    def do_nothing(self): # Back from when it did nothing
        if not self.charged:
            print(f"{self.first_name} is charging")
            self.charged = True
        else:
            print(f"{self.first_name} is already charged!")
        if self.mana < self.max_mp:
            self.mana += 1
            print(f"{self.first_name} also regained 1 mana!")
        else:
            print(f"{self.first_name} is at full mana!")

    # To decrease damage
    def defend(self):
        print(f"{self.first_name} is defending!")
        self.guard = True

    def turn(self):
        # Player turn

        print("It's your turn! What do you want to do?")
        print()
        print(self.first_name, self.surname)
        print(f"[red]HP: {self.hp}[/red]/[red]{self.max_hp}[/red] || [blue]Mana: {self.mana}[/blue]/[blue]{self.max_mp}[/blue] || ", end="")
        if self.charged:
            print("[yellow]Charged!")
        else:
            print("[yellow]Not charged!")
        print()
        print("1) Attack")
        print("2) Defend")
        print("3) Charge")
        print()
        choice = ""
        while True:
            choice = input("What do you do? ").strip().lower()
            if choice == "1" or choice == "attack":
                for i in range(len(self.moves)):
                    print(self.moves[i-1].name)
                choice = input("Which attack do you use? (type 'back' to go back) \n").lower().strip()
                for i in range(len(self.moves)):
                    if self.moves[i-1].name.lower() == choice:
                        choice = self.moves[i-1]
                        choice = self.moves.index(choice)
                        print()
                        return(self.moves[choice].use_wpn(player, e))

                    elif choice == "back":
                        print()

                    else:
                        print("Attack not recognized")
            
            elif choice == "2" or choice == "defend":
                self.defend()
                return

            elif choice == "3" or choice == "charge":
                self.do_nothing()
                return

            else:
                print(f"Choice {choice} not recognized, try again")

    def level_up(self):
        print(f"{self.first_name} {self.surname} has leveled up!")

        new_val = 3 + math.floor(self.strength * 2)
        print(f"{self.first_name} got {new_val} max HP!")
        self.max_hp += new_val

        new_val = 1 + math.floor(self.strength * 1.1)
        print(f"{self.first_name} got {new_val} max MP!")
        self.max_mp += new_val

        print(f"Since {self.first_name}  {self.surname} leveled up, they get a boon!")
        print()
        print(f"1) +1 strenght point")
        print(f"2) +D4 max HP")
        print(f"3) +D2 max Mana")
        choice = input("What do you pick? ")
        while True:
            if choice == "1":
                self.strength_point += 0.25
                print(f"Gained 1 strenght point")
                if self.strength_point == 1:
                    print(f"Full strenght achieved! Now at {self.strength}")
                    self.strength_point = 0
                    self.strength += 1
                break
            elif choice == "2":
                new_val = random.randint(1,4)
                print(f"Gained {new_val} max HP!")
                break
            elif choice == "3":
                new_val = random.randint(1,2)
                print(f"Gained {new_val} max Mana!")
                break
            print(f"Boon {choice} not recognized")

        for i in range(len(self.lvl_rewards_no)):
            if self.lvl_rewards_no[i-1] == self.level:
                print(f"{self.first_name}  {self.surname} has learned a new move! They got {self.lvl_rewards[i-1]}")
                list.append(self.moves, self.lvl_rewards[i-1])

        print("HP and Mana fully restored")
        self.hp = self.max_hp
        self.mana = self.max_mp
        self.level += 1
    
    def fix_stf(self):
        if self.mana > self.max_mp:
            self.mana = self.max_mp
        if self.hp > self.max_hp:
            self.hp = self.max_hp


moves_list = []
# set up moves
def makeMove(name, mana, up_dmg, dwn_dmg, dmg, hit_plus, hits, type):
    # print(name, mana, up_dmg, dwn_dmg, dmg, hit_plus, hits, type)
    moves_list.append([name, mana, up_dmg, dwn_dmg, dmg, hit_plus, hits, type])
    return Moves(name, mana, up_dmg, dwn_dmg, dmg, hit_plus, hits, type)

slash = makeMove("Slash", 0, 1, -1, 3, 1, 1, "attack")
multiStab = makeMove("MultiStab", 5, 2, -3, 4, -2, 5, "attack")
dummy_blast = makeMove("Dummy Blast", 0, 0, 0, 999, 999, 1, "attack")
shiv = makeMove("Shiv", 0, 3, 0, 1, 0, 1 , "attack")
smack = makeMove("Smack", 0, 3, 0, 2, 0, 1, "attack")
pebbles = makeMove("Pebbles", 0, 1, 0, 0, -1, 3, "attack")
smnBoulder = makeMove("Summon Boulder. Like that's literally a boulder, a physical boulder! This isn't any hehehaha boulder, if this hits you, you're DEAD. So anyway... Summon Boulder", 99, 99, -99, 200, -10, 1, "attack")

# Make enemy

enemies = [0, 1, 2, 3]
def make_enemy(type, level):
    global e
    if type == 0:
        e = Enemy("Target Dummy", "the IV", 15, 0, 1, 11, [dummy_blast], 0, dummy_AI, False, 1, level, 1)
    if type == 1:
        e = Enemy("Goblin", "Thief", 12, 5, 1, 14, [shiv, multiStab], 0, goblin_AI, False, 5, level, random.randint(5, 7))
    if type == 2:
        e = Enemy("Target Smarty", "McPants", 7, 0, -1, 8, [smack], 0, dummy_AI, True, 1, level, 1)
    if type == 3:
        e = Enemy("Goblin", "Rock",20, 99, 5, 17, [pebbles, smnBoulder], 0, rock_AI, False, 10, level, 15)
    
    for i in range(level-1):
        e.level_up
    
# Set up character
print()
name = input("What will be the first name of your character? \n").strip()
surname = input("And what about their last name? \n").strip()
if name == "":
    name = "Blinko"

if surname == "":
    surname = "Shmlinko"

player = Player(name, surname, 20, 5, 3, 13, 0, [slash], 0, 1, -100)
make_enemy(2,1)



def crossroads():
    print(f"In front of you there are 2 paths.")

    




do_combat(player, e)

while True:
    print()
    if player.is_alive():
        print(f"{player.first_name} {player.surname} wins!")
        player.shmeckle += e.shmeckle
        print(f"{player.first_name} got {e.shmeckle} Shmeckles!")
        print(f"{player.first_name} gained {e.xp} xp!")
        player.xp += e.xp
        player.tot_xp += e.xp
        while player.xp >= player.xp_til_level_up:
            player.level_up()
            player.xp -= player.xp_til_level_up
            player.xp_til_level_up = math.floor(player.xp_til_level_up * 1.3) + math.floor(player.level / 5)

        print()

        print("Starting new combat...")

        temp = random.randint(1, len(enemies)-1)
        print(temp)
        make_enemy(temp, 1)
        do_combat(player, e)
    elif not player.is_alive():
        print(f"{player.first_name} {player.surname} is defeated...")
        print("[red]GAME OVER")
        break
    else:
        print("No victor")