import random
from World.Organism.Animal.Animal import Animal


class Antelope(Animal):
    def __init__(self, world=None, pos=None):
        super().__init__()
        self.strength = 4
        self.initiative = 4
        self.movement_speed = 1
        self.set_sign('A')
        self.set_name("Antelope")
        if world and pos:
            self.set_world(world)
            self.set_position(pos.x, pos.y)

    def special_attack(self, attack, defend):
        dodge_chance = random.randint(0, 3)

        if dodge_chance < 2:
            return False
        else:
            helping = [0] * 4
            self.find_safe(helping)

            counter = sum(1 for i in helping if i == 1)

            if counter == 0:
                return False
            else:
                while True:
                    random_position = random.randint(0, 3)

                    if helping[random_position] == 1:
                        self.set_movement_speed(0)
                        self.move(random_position)
                        self.set_movement_speed(1)
                        self.set_moved(True)
                        self.world.write_text("Antelope has escaped from the fight!\n")
                        break

                return True
