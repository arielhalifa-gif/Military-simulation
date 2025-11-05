from abc import ABC, abstractmethod

class Weapon:
    total_weapons = 0

    def __init__(self, name: str, ammo: int):
        self.name = name
        self.ammo = ammo
        Weapon.total_weapons += 1

class Soldier:
    def __init__(self, name: str, rank: str, weapon: Weapon):
        self.name = name
        self.rank = rank
        self.weapon = weapon

    def report(self): #מדפיס את הפרטים של החייל
        print(f"name: {self.name}\nrank: {self.rank}")


class Unit(ABC):
    def __init__(self, unit_name: str, comander: Soldier, soldiers: list[Soldier], strike_options: list):
        self.name_unit = unit_name
        self.comander = comander
        self.soldiers = soldiers
        self.strike_options = strike_options

    def briefing(self):
        print(f"unit: -> {self.name_unit}")
        self.comander.report()

    @abstractmethod
    def attack(self):
        pass


class Infantry(Unit):
    def attack(self):
        print(f"infantry unit strike")

class TankUnit(Unit):
    def attack(self):
        print(f"tank unit strike")

class Sniper(Unit):
    def attack(self):
        print(f"sniper units atack")
