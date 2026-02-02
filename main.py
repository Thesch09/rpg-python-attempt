from rich import print
from AI_module import dummy_AI
from AI_module import goblin_AI
# from oppgave_6_NPC_module import enemyList
import random
import math
import time



class Moves:
    # Create move
    def __init__(self, name, mana, up_dmg, dwn_dmg, dmg, hit_plus, hits, type):
        self.name = name
        self.mana = mana
        # up_dmg and dwn_dmg are how much a move can deal additionally
        self.up_dmg = up_dmg
        self.dwn_dmg = dwn_dmg
        self.dmg = dmg
        self.hits = hits
        self.hit_plus = hit_plus
        self.type = type

    def use_wpn(self, user, target):
        if self.type == "attack":
            print(f"{user.first_name} is attempting to use {self.name} on {target.first_name}!")
            
            if user.mana < self.mana:
                print(f"{user.first_name} doesn't have enough mana to use this move!")
                return
            user.mana -= self.mana
            print(f"{user.first_name} used {self.mana} mana")

            dice = random.randint(1, 20)
            print(f"{user.first_name} rolls a {dice}")
            print(f"With {self.name}'s bonus to hit it's {dice + self.hit_plus}")

            # We do love our chances
            
            if self.hits < 2:
                self.hits = 1
            damage_buff = 1
            if user.charged:
                damage_buff *= 1.3

            if dice == 20:
                print(f"{user.first_name} crits {target.first_name}!!!")
                damage_buff *= 1.5
                if not self.hits > 1:
                    self.hits = 0
                for i in range(random.randint(1, self.hits+1)):
                    target.take_damage(self.dmg * damage_buff + random.randint(self.dwn_dmg + 1, self.up_dmg + 1))
                    time.sleep(0.5)
            elif dice + self.hit_plus >= target.ac:
                for i in range(random.randint(1, self.hits)):
                    target.take_damage(self.dmg * damage_buff + random.randint(self.dwn_dmg, self.up_dmg))
                    time.sleep(0.5)
            elif dice == 1:
                print(f"{user.first_name} critically missed!")
            else:
                print(f"{user.first_name} misses")
            if user.charged:
                user.charged = False
                print(f"{user.first_name} is no longer charged!")

class Enemy:
    # Create the Enemy
    def __init__(self, first_name, surname, max_hp, max_mp, strength, ac, moves, special, AI, charged):
        self.first_name = first_name
        self.surname = surname
        self.max_hp = max_hp
        self.hp = self.max_hp
        self.max_mp = max_mp
        self.mana = self.max_mp
        self.strength = strength
        self.ac = ac
        self.guard = False
        self.moves = moves
        self.special = special
        self.AI = AI
        self.charged = charged

    
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
    def do_nothing(self):
        print(f"{self.first_name} does nothing")

    # To decrease damage
    def defend(self):
        print(f"{self.first_name} is defending!")
        self.guard = True

    def charge(self): # Back from when it did nothing
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



class Player:
    # Create character
    def __init__(self, first_name, surname, max_hp, max_mp, strength, ac, charged, moves):
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

# Player turn
def player_turn():
    print("It's your turn! What do you want to do?")
    print()
    print(player.first_name, player.surname)
    print(f"[red]HP: {player.hp}[/red]/[red]{player.max_hp}[/red] || [blue]Mana: {player.mana}[/blue]/[blue]{player.max_mp}[/blue] || ", end="")
    if player.charged:
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
        choice = input("What do you do? ")
        if choice == "1":
            for i in range(len(player.moves)):
                print(player.moves[i-1].name)
            choice = input("Which attack do you use? (type 'back' to go back) \n").lower().strip()
            for i in range(len(player.moves)):
                if player.moves[i-1].name.lower() == choice:
                    choice = player.moves[i-1]
                    choice = player.moves.index(choice)
                    print()
                    return(player.moves[choice].use_wpn(player, e))

                elif choice == "back":
                    print()

                else:
                    print("Attack not recognized")
        
        elif choice == "2":
            return(player.defend())

        elif choice == "3":
            return(player.do_nothing())

        else:
            print(f"Choice {choice} not recognized, try again")

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
def make_enemy(type):
    if type == 0:
        return Enemy("Target Dummy", "the IV", 15, 0, 1, 11, [dummy_blast], 0, dummy_AI, False)
    if type == 1:
        return Enemy("Goblin", "Thief", 12, 5, 1, 14, [shiv, multiStab], 0, goblin_AI, False)

# Set up character
print()
name = input("What will be the first name of your character? \n").strip()
surname = input("And what about their last name? \n").strip()
if name == "":
    name = "Blinko"

if surname == "":
    surname = "Shmlinko"

player = Player(name, surname, 20, 5, 3, 13, 0, [slash, multiStab])
e = make_enemy(0)

def do_combat(player, e):
    print(player.first_name, player.surname, player.hp)
    print(e.first_name, e.surname, e.hp)
    turn_count = 1

    while player.is_alive() and e.is_alive():
        print()
        print()
        print(f"It is turn number {turn_count}")
        time.sleep(1)
        print()

        # Player action
        player_turn()
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
    print(f"{player.first_name + " " + player.surname} wins!")
    print()
    print("Starting new combat...")
    e = make_enemy(random.randint(0, len(enemies)-1))
    do_combat(player, e)
elif not player.is_alive():
    print(f"{player.first_name + " " + player.surname} is defeated...")
    print("[red]GAME OVER")
else:
    print("No victor")