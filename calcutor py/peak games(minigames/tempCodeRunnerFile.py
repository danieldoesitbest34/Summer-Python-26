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