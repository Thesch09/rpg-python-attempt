import random
import time
import math
from rich import print

class Moves:
    # Create move
    def __init__(self, name, mana, up_dmg, dwn_dmg, dmg, hit_plus, min_hits, hits, cw, type):
        self.name = name
        self.mana = mana
        # up_dmg and dwn_dmg are how much a move can deal additionally
        self.up_dmg = up_dmg
        self.dwn_dmg = dwn_dmg
        self.dmg = dmg
        self.min_hits = min_hits
        self.hits = hits
        self.hit_plus = hit_plus
        self.type = type
        self.cw_max = cw
        self.cw = 0

    def use_wpn(self, user, target):
        if self.type == "attack":
            print(f"{user.first_name} is attempting to use {self.name} on {target.first_name}!")
            
            if user.mana < self.mana:
                print(f"{user.first_name} doesn't have enough mana to use this move!")
                return
            user.mana -= self.mana
            print(f"{user.first_name} used {self.mana} mana")

            if self.cw > 0:
                print(f"But it's on cooldown! ({self.cw})")
            self.cw = self.cw_max

            dice = random.randint(1, 20)
            print(f"{user.first_name} rolls a {dice}")
            if self.hit_plus > 0:
                print(f"With {self.name}'s bonus to hit it's {dice + self.hit_plus}")
            elif self.hit_plus < 0:
                print(f"With {self.name}'s reduction to hit it's {dice + self.hit_plus}")

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
                    target.take_damage(math.ceil(self.dmg * damage_buff + random.randint(self.dwn_dmg + 1, self.up_dmg + 1)))
                    time.sleep(0.5)
            elif dice + self.hit_plus >= target.ac:
                for i in range(random.randint(1, self.hits)):
                    target.take_damage(math.floor(self.dmg * damage_buff + random.randint(self.dwn_dmg, self.up_dmg)))
                    time.sleep(0.5)
            elif dice == 1:
                print(f"{user.first_name} critically missed!")
            else:
                print(f"{user.first_name} misses")
            if user.charged:
                user.charged = False
                print(f"{user.first_name} is no longer charged!")
    
    def cooldown(self):
        if self.cw_max == -1:
            print("UNCOOLDOWNABLE")