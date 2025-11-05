from Army_Inventory import Weapon, Soldier, Unit

class StrikeOption:
    def __init__(self, name: str, ammo: int):
        self.name = name
        self.ammo = ammo

    def strike(self):
        pass

class Tank(StrikeOption):
    def strike(self):
        print(f"this tank name is -> {self.name}")


class Drone(StrikeOption):
    def strike(self):
        print(f"the drone name is -> {self.name}")


# unit1 = Unit("7160", commander, [soldier1,soldier2,soldier3], [tank1,tank2,drone1,drone2])
# for unit in unit1.strike_options:
#     print(unit)


