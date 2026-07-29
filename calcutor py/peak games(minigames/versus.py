import random
import time

class Brawler:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def attack(self, opponent):
        damage = random.randint(1, self.strength)
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} and deals {damage} damage.")

    def is_alive(self):
        return self.health > 0
    
class CM_Punk(Brawler):
     def __init__(self, name, health, strength, Lighting_skill):
        super()._init_(name, health, strength)
        self.sword_skill = GTS_skill
    
    def attack(self, opponent):
        damage = random.randint(self.sword_skill, self.strength)
        opponent.health -= damage
        print(f"{self.name} when CM_Punk pops his ult he deals 40{damage} damage to {opponent.name}.")

class Tank:
     def __init__(self, name, health, strength):
          self.name = name
          self.health = health
          self.strength = strength

     def attack(self, opponent):
          damage = random.randint