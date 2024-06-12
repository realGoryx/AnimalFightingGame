import random
import math
from World.Organism.Animal.Animal import Animal
from World.Position import Position


class Cybersheep(Animal):
    def __init__(self, world=None, pos=None):
        super().__init__()
        self.strength = 11
        self.initiative = 4
        self.sign = 'C'
        self.name = "Cybersheep"
        if world and pos:
            self.world = world
            self.position = pos

    def action(self):
        sosnowsky_pos = []
        sos_count = self.world.count_sos()
        sosnowsky_pos = self.world.get_sosnowskys_position()

        cyber_pos = self.get_position()
        cyber_x = cyber_pos.x
        cyber_y = cyber_pos.y

        min_distance = float('inf')
        closest_x = 0
        closest_y = 0

        for pos in sosnowsky_pos:
            distance = math.sqrt((cyber_x - pos.x) ** 2 + (cyber_y - pos.y) ** 2)
            if distance < min_distance:
                min_distance = distance
                closest_x = pos.x
                closest_y = pos.y

        if sos_count > 0:
            if cyber_x != closest_x:
                if cyber_x > closest_x:
                    if self.world.return_symbol(cyber_x - 1, cyber_y) == '*':
                        self.move(1)
                    else:
                        attacking = Position(cyber_x - 1, cyber_y)
                        outcome = self.collision(attacking)

                        if outcome == 6:
                            self.move(1)
                elif cyber_x < closest_x:
                    if self.world.return_symbol(cyber_x + 1, cyber_y) == '*':
                        self.move(0)
                    else:
                        attacking = Position(cyber_x + 1, cyber_y)
                        outcome = self.collision(attacking)

                        if outcome == 6:
                            self.move(0)
            elif cyber_y != closest_y:
                if cyber_y > closest_y:
                    if self.world.return_symbol(cyber_x, cyber_y - 1) == '*':
                        self.move(3)
                    else:
                        attacking = Position(cyber_x, cyber_y - 1)
                        outcome = self.collision(attacking)

                        if outcome == 6:
                            self.move(3)
                elif cyber_y < closest_y:
                    if self.world.return_symbol(cyber_x, cyber_y + 1) == '*':
                        self.move(2)
                    else:
                        attacking = Position(cyber_x, cyber_y + 1)
                        outcome = self.collision(attacking)

                        if outcome == 6:
                            self.move(2)
        else:
            super().action()