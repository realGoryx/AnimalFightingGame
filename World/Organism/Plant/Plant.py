from abc import ABC, abstractmethod
import random

from World.Organism.Organism import Organism


class Plant(Organism):
    def __init__(self):
        super().__init__()

    def action(self):
        self.years_old += 1

        if self.years_old < 3:
            return

        helping = [0, 0, 0, 0]
        count = 0

        self.find_safe(helping)

        for i in range(4):
            if helping[i] == 1:
                count += 1

        if count == 0:
            return

        chance = random.randint(0, 99)

        if chance < 80:
            return
        else:
            while True:
                random_position = random.randint(0, 3)

                if helping[random_position] == 1:
                    self.sowing(random_position)
                    return

    def find_safe(self, help_array):
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        posX = self.position.get_x()
        posY = self.position.get_y()

        for i in range(4):
            if self.world.return_symbol(posX + dx[i], posY + dy[i]) == '*':
                help_array[i] = 1
            elif self.world.return_symbol(posX + dx[i], posY + dy[i]) == '?':
                help_array[i] = 2

    def sowing(self, direction):
        posX = self.position.get_x()
        posY = self.position.get_y()

        direct = direction
        # 0 - down, 1 - up, 2 - right, 3 - left

        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        new_pos_x = posX + dx[direct]
        new_pos_y = posY + dy[direct]

        if new_pos_x >= self.world.get_height() or new_pos_x < 0 or new_pos_y >= self.world.get_width() or new_pos_y < 0:
            return
        elif self.world.return_symbol(new_pos_x, new_pos_y) != '*':
            return

        self.world.add_organism_to_board(new_pos_x, new_pos_y, self.get_sign())
        self.world.write_text(self.get_name() + " has been sowed!\n")

    def collision(self, attacking):
        return 99
