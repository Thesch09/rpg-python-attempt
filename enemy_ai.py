import random

def dummy_AI(self, target):
    print(f"{self.first_name + " " + self.surname} is going to do something...")
    print()

    choice = random.randint(1,4)
    if self.special == 3:
        print(f"{self.first_name} is  blasting a huge blast at {target.first_name}!")
        self.moves[0].use_wpn(self, target)
        return(True)
    elif self.hp < 6:
        self.special += 1
        print(f"{self.first_name} is charging a huge attack!")
    elif choice == 4:
        self.defend()
    else:
        self.do_nothing()

def goblin_AI(self, target):
    print(f"{self.first_name + " " + self.surname} is going to do something...")
    print()

    choice = random.randint(1,6)
    if self.mana >= 5:
        print(f"{self.first_name} is  using {self.moves[1].name} on {target.first_name}!")
        self.moves[1].use_wpn(self, target)
        return(True)
    elif choice == 6 or self.mana == 0:
        self.charge()
    elif choice > 3:
        self.defend()
    else:
        self.moves[0].use_wpn(self, target)

def rock_AI(self, target):
    print(f"There is a {self.surname} of the {self.first_name} variety here.")
    print()

    choice = random.randint(1,100)
    if choice == 100 and self.mana == 99:
        self.moves[1].use_wpn(self, target)
    elif choice > 73:
        self.moves[0].use_wpn(self, target)
        self.mana += 5
    elif choice >= 20:
        self.defend()
    else:
        self.do_nothing()
        self.mana += 1