from Army_Inventory import Unit
from abc import ABC, abstractmethod

class Agent:
    def __init__(self, codename: str, clearence_level: int):
        self.codename = codename
        self.clearence_level = clearence_level


class Mission(ABC):
    def __init__(self, mission_name: str, target: str, assigned_agent: Agent, assigned_unit: Unit):
        self.mission_name = mission_name
        self.target = target
        self.assigned_agent = assigned_agent
        self.unit = assigned_unit

    def briefing(self):
        print(f"mission details: name:{self.mission_name}, target: {self.target}")
        print(f"agent name -> {self.assigned_agent}")

class MissionManager:
    missions = []
    @classmethod
    def add_mission(cls, mission: Mission):
        MissionManager.missions.append(mission)
        print(f"mission added succesguly")

    def remove_mission(self, mission):
        MissionManager.missions.remove(mission)
        print(f"mission removed succesfuly")

class ReconMission(Mission):
    def execute(self):
        for i in self.unit.strike_options:
            i.strike()
            self.unit.attack()


class StrikeMission(Mission):
    def execute(self):
        for i in self.unit.strike_options:
            i.strike()
            self.unit.attack()

class RescueMission(Mission):
    def execute(self):
        for i in self.unit.strike_options:
            i.strike()
            self.unit.attack()