import random
from World.Organism.Animal.Animal import Animal


class Fox(Animal):
    def __init__(self, world=None, pos=None):
        super().__init__()
        self.strength = 3
        self.initiative = 7
        self.set_sign('F')
        self.set_name("Fox")
        if world and pos:
            self.set_world(world)
            self.set_position(pos.x, pos.y)

    def action(self):
        self.years_old += 1

        helping = [0] * 4
        self.find_safe(helping)
        quit = False

        while not quit:
            random_position = random.randint(0, 3)

            if helping[random_position] == 1:
                self.move(random_position)
                quit = True
            elif helping[random_position] == 2:
                # Do nothing
                pass
            else:
                dy = [0, 0, 1, -1]
                dx = [1, -1, 0, 0]

                next_pos_x = self.position.x + dx[random_position]
                next_pos_y = self.position.y + dy[random_position]

                if self.world.get_organism(next_pos_x, next_pos_y).strength > self.strength:
                    self.world.write_text("Fox has sensed the danger and stayed in place!\n")
                    return

                outcome = self.collision(self.world.get_organism(next_pos_x, next_pos_y).position)
                if outcome == 6:
                    self.move(random_position)
                    break
