from rich import print
from enemy_ai import dummy_AI
from enemy_ai import goblin_AI
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

        new_val = 3 + math.floor(self.strength) * 2
        print(f"{self.first_name} got {new_val} max HP!")
        self.max_hp += new_val

        new_val = 3 + math.floor(self.strength) * 1.1
        print(f"{self.first_name} got {new_val} max MP!")
        self.max_mp += new_val

        print(f"Since {self.first_name}  {self.surname} leveled up, they can get a boon!")
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

        print("HP and Mana fully restored")
        self.hp = self.max_hp
        self.mana = self.max_mp
        self.level += 1


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

# Make enemy

enemies = [0, 1]
def make_enemy(type, level):
    global e
    if type == 0:
        e = Enemy("Target Dummy", "the IV", 15, 0, 1, 11, [dummy_blast], 0, dummy_AI, False, 1, level, 1)
    if type == 1:
        e = Enemy("Goblin", "Thief", 12, 5, 1, 14, [shiv, multiStab], 0, goblin_AI, False, 5, level, random.randint(5, 7))
    
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

player = Player(name, surname, 20, 5, 3, 13, 0, [slash, multiStab], 0, 1)
make_enemy(0,1)

def do_combat(player, e):

    print(f"{player.first_name} {player.surname}, [red]{player.hp} HP[/red], level {player.level}")
    print("VS")
    print(f"{e.first_name} {e.surname}, [red]{e.hp} HP[/red], level {player.level}")
    turn_count = 1

    while player.is_alive() and e.is_alive():
        print()
        print()
        print(f"It is turn number {turn_count}")
        time.sleep(1)
        print()

        # Player action
        player.turn()
        time.sleep(0.5)
        if not e.is_alive():
            break
        print()

        # Enemy action
        # Un-hardcode it <- done <- Less done <- More done

        e.AI(e, player)
            
        time.sleep(0.5)
        print()
        
        # Increase turn_count so the fight doesn't last forever
        turn_count += 1
        if turn_count > 50:
            print("The battle ran out of time!")
            return

do_combat(player, e)

print()
if player.is_alive():
    print(f"{player.first_name} {player.surname} wins!")
    print(f"{player.first_name} gained {e.xp} xp!")
    player.xp += e.xp
    player.tot_xp += e.xp
    if player.xp == player.xp_til_level_up:
        player.level_up()
        player.xp = 0
        player.xp_til_level_up = math.floor(player.xp_til_level_up * 1.3) + math.floor(player.level / 5)

    print()

    print("Starting new combat...")
    make_enemy(random.randint(0, len(enemies)-1), 1)
    do_combat(player, e)
elif not player.is_alive():
    print(f"{player.first_name} {player.surname} is defeated...")
    print("[red]GAME OVER")
else:
    print("No victor")