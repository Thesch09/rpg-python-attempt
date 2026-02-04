import math
from rich import print

class Enemy:
    # Create the Enemy
    def __init__(self, first_name, surname, max_hp, max_mp, strength, ac, moves, special, AI, charged, xp, level, shmeckle):
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
        self.xp = xp
        self.level = level
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
        if self.hp <= 0:
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
    def level_up(self):
        self.max_hp += 3 + self.strength * 2
        self.max_mp += 1 + math.floor(self.strength * 1.1)
        self.hp = self.max_hp
        self.mana = self.max_mp
    
    def fix_stf(self):
        if self.mana > self.max_mp:
            self.mana = self.max_mp
        if self.hp > self.max_hp:
            self.hp = self.max_hp
