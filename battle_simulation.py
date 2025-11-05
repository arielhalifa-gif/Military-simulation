from Army_Inventory import Unit, Infantry, TankUnit, Sniper, Weapon, Soldier
from Strike_Options import Tank, Drone

class Army:
    total_attacks = 0
    def __init__(self, units: list[Unit]):
        self.units = units

    def attack_all(self):
        for a in self.units:
            a.attack()
            Army.total_attacks += 1

tank1 = Tank("mercava", 4)
tank2 = Tank("namer", 5)
drone1 = Drone("sky_vision", 10)
drone2 = Drone("red_wings", 6)
w1 = Weapon("rpg", 1)
w2 = Weapon("uzi", 15)
w3 = Weapon("m416", 50)
w4 = Weapon("m16", 100)
w5 = Weapon("calachnicov", 150)
w6 = Weapon("m2mini", 50)
soldier1 = Soldier("moshe","turai", w1)
soldier2 = Soldier("abraham", "samal", w2)
soldier3 = Soldier("yosi", "turai", w3)
soldier4 = Soldier("moshe","turai", w1)
soldier5 = Soldier("abraham", "samal", w2)
soldier6 = Soldier("yosi", "turai", w3)
commander = Soldier("baruj", "commander", w1)
commander2 = Soldier("beni", "commander", w3)
commander3 = Soldier("dudu", "commander", w6)
in1 = Infantry("kfir", commander, [soldier1, soldier2, soldier3],[tank1, tank2, drone1, drone2])
t1 = TankUnit("tankistim", commander2, [soldier4, soldier5, soldier2],[tank1, drone2])
s1 = Sniper("kala", commander3, [soldier6, soldier3, soldier1], [drone1, tank2])

army1 = Army([in1, t1, s1])
army1.attack_all()