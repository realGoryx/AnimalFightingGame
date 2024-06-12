from World.Organism.Plant.Plant import Plant
from World.Organism.Animal.Animal import Animal


class SosnowskyHogweed(Plant):
    def __init__(self, world=None, pos=None):
        super().__init__()
        self.strength = 10
        self.initiative = 0
        self.set_sign('+')
        self.set_name("Sosnowsky")
        if world and pos:
            self.set_position(pos.x, pos.y)
            self.set_position(pos.x, pos.y)

    def action(self):
        dy = [0, 0, -1, 1]
        dx = [1, -1, 0, 0]

        prey = None

        animal = ['T', 'F', '@', 'W', 'S', 'A']

        for i in range(4):
            test_sign = self.world.return_symbol(self.get_position().get_x() + dx[i], self.get_position().get_y() + dy[i])

            for j in range(6):
                if test_sign == animal[j]:
                    pos_x = self.get_position().get_x() + dx[i]
                    pos_y = self.get_position().get_y() + dy[i]

                    prey = self.world.get_organism(pos_x, pos_y)
                    self.world.kill_organism(prey, pos_x, pos_y)
                    self.world.write_text("Sosnowsky Hogweed has poisoned and killed " + prey.get_name() + "\n")
                    break

        super().action()
