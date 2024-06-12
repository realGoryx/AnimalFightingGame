import random
from World.Organism.Animal.Animal import Animal
import time


class Turtle(Animal):
    def __init__(self, world=None, pos=None):
        super().__init__()
        self.strength = 2
        self.initiative = 1
        self.set_sign('T')
        self.set_name("Turtle")
        if world and pos:
            self.set_world(world)
            self.set_position(pos.x, pos.y)

    def action(self):
        self.years_old += 1
        chance = random.randint(0, 3)

        if chance < 2:
            super().action()

    def special_attack(self, attack, defend):
        if self == defend and attack.strength > 5:
            return False
        elif self == defend and attack.strength < 5:
            self.world.write_text("Turtle has blocked the attack!")
            time.sleep(1)
            return True
        else:
            return False