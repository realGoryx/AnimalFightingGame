from abc import ABC, abstractmethod
import random

from World.Organism.Organism import Organism


class Animal(Organism, ABC):
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
                # Out of map!
                # quit = True
                pass
            else:
                dy = [0, 0, 1 + self.movement_speed, -1 - self.movement_speed]
                dx = [1 + self.movement_speed, -1 - self.movement_speed, 0, 0]

                outcome = self.collision(self.world.get_organism(
                    self.position.x + dx[random_position],
                    self.position.y + dy[random_position]
                ).position)

                if outcome == 6:
                    self.move(random_position)
                    break
                else:
                    break

    def collision(self, attacking_pos):
        defender = self.world.get_organism(attacking_pos.x, attacking_pos.y)

        if defender:
            if (defender.get_sign() == self.get_sign() and
                    self.get_years() > 3 and
                    defender.get_years() > 3):

                helping = [0] * 8
                self.find_safe(helping)
                self.find_safe_two(helping, attacking_pos)
                counter = sum(1 for i in helping if i == 1)

                if counter == 0:
                    return 99

                while True:
                    random_position = random.randint(0, 7)

                    if helping[random_position] == 1:
                        if random_position < 4:
                            self.breed(random_position, self.position, self.get_sign())
                            return 99
                        else:
                            random_position -= 4
                            self.breed(random_position, attacking_pos, self.get_sign())
                            return 99
            elif defender.get_sign() != self.get_sign():
                if defender.get_sign() == '+' and self.get_sign() == 'C':
                    self.world.kill_organism(defender, attacking_pos.x, attacking_pos.y)
                    self.world.write_text(f"{self.get_name()} has killed {defender.get_name()}\n")
                    return 6

                if defender.special_attack(self, defender):
                    if defender.get_sign() in ['G', 'A']:
                        return 6
                    return 5
                if self.special_attack(self, defender):
                    return 4
                if defender.get_strength() > self.get_strength():
                    self.world.kill_organism(self, self.position.x, self.position.y)
                    self.world.write_text(f"{defender.get_name()} has killed {self.get_name()}\n")
                    return 1
                else:
                    self.world.kill_organism(defender, attacking_pos.x, attacking_pos.y)
                    self.world.write_text(f"{self.get_name()} has killed {defender.get_name()}\n")
                    return 6
        return 0

    def move(self, direction):
        pos_x = self.position.x
        pos_y = self.position.y

        movement_speed = self.movement_speed

        dy = [0, 0, 1 + movement_speed, -1 - movement_speed]
        dx = [1 + movement_speed, -1 - movement_speed, 0, 0]

        self.position.x += dx[direction]
        self.position.y += dy[direction]

        self.world.help_animal_move(self, self.position.x, self.position.y)
        self.world.erase_organism(pos_x, pos_y)

        self.world.write_text(f"{self.get_name()} has moved to {self.position.x}, {self.position.y}\n")

    def breed(self, direction, pos, sign):
        pos_x = pos.x
        pos_y = pos.y

        dy = [0, 0, 1, -1]
        dx = [1, -1, 0, 0]

        new_pos_x = pos_x + dx[direction]
        new_pos_y = pos_y + dy[direction]

        if (new_pos_x >= self.world.get_height() or new_pos_x < 0 or
                new_pos_y >= self.world.get_width() or new_pos_y < 0):
            return
        elif self.world.return_symbol(new_pos_x, new_pos_y) != '*':
            return

        self.world.add_organism_to_board(new_pos_y, new_pos_x, sign)
        self.world.write_text(f"{self.get_name()} has been bred!\n")

    def find_safe(self, help_array):
        dy = [0, 0, 1 + self.movement_speed, -1 - self.movement_speed]
        dx = [1 + self.movement_speed, -1 - self.movement_speed, 0, 0]

        pos_x = self.position.x
        pos_y = self.position.y

        for i in range(4):
            symbol = self.world.return_symbol(pos_x + dx[i], pos_y + dy[i])
            if symbol == '*':
                help_array[i] = 1
            elif symbol == '?':
                help_array[i] = 2

    def find_safe_two(self, help_array, attacking_pos):
        dy = [0, 0, 1, -1]
        dx = [1, -1, 0, 0]

        pos_x = attacking_pos.x
        pos_y = attacking_pos.y

        for i in range(4):
            symbol = self.world.return_symbol(pos_x + dx[i], pos_y + dy[i])
            if symbol == '*':
                help_array[i] = 1
            elif symbol == '?':
                help_array[i] = 2