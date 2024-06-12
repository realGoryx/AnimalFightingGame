import random

import tkinter as tk
from tkinter import ttk

from World.Organism.Animal.Animal import Animal


class Human(Animal):
    def __init__(self, world=None, pos=None):
        super().__init__()
        self.strength = 5
        self.initiative = 4
        self.set_name("Human")
        self.set_world(world)
        self.set_position(pos.x, pos.y)
        self.set_sign('@')
        self.rounds_after_special = 0
        self.used_special = False

    def move_up(self):
        if self.world.return_symbol(self.position.x - 1, self.position.y) == '?':
            print(self.position.x)
            return
        elif self.world.return_symbol(self.position.x - 1, self.position.y) == '*':
            self.count_special()
            self.erase_traces(self.position.x - 1, self.position.y)
            return
        else:
            check_collision = super().collision(self.world.get_organism(self.position.x - 1, self.position.y).position)
            if check_collision == 6:
                self.erase_traces(self.position.x - 1, self.position.y)
            return

    def move_down(self):
        if self.world.return_symbol(self.position.x + 1, self.position.y) == '?':
            return
        elif self.world.return_symbol(self.position.x + 1, self.position.y) == '*':
            self.count_special()
            self.erase_traces(self.position.x + 1, self.position.y)
            return
        else:
            check_collision = super().collision(self.world.get_organism(self.position.x + 1, self.position.y).position)
            if check_collision == 6:
                self.erase_traces(self.position.x + 1, self.position.y)
            return

    def move_left(self):
        if self.world.return_symbol(self.position.x, self.position.y - 1) == '?':
            return
        elif self.world.return_symbol(self.position.x, self.position.y - 1) == '*':
            self.count_special()
            self.erase_traces(self.position.x, self.position.y - 1)
            return
        else:
            check_collision = super().collision(self.world.get_organism(self.position.x, self.position.y - 1).position)
            if check_collision == 6:
                self.erase_traces(self.position.x, self.position.y - 1)
            return

    def move_right(self):
        if self.world.return_symbol(self.position.x, self.position.y + 1) == '?':
            return
        elif self.world.return_symbol(self.position.x, self.position.y + 1) == '*':
            self.count_special()
            self.erase_traces(self.position.x, self.position.y + 1)
            return
        else:
            check_collision = super().collision(self.world.get_organism(self.position.x, self.position.y + 1).position)
            if check_collision == 6:
                self.erase_traces(self.position.x, self.position.y + 1)
            return

    def action(self):
        pos_x = self.position.x
        pos_y = self.position.y

        while True:
            arrow = input("Press s to start the game!").strip().lower()
            if arrow == 's':
                return
            elif arrow == 'e':
                if not self.used_special:
                    self.special_ability(self.position.x, self.position.y)
                return
            elif arrow == 'q':
                self.world.set_saved(True)
                return
            elif arrow == 'l':
                self.world.load_game_status()
                return

    def count_special(self):
        if self.used_special:
            self.rounds_after_special += 1
            if self.rounds_after_special < 5:
                self.world.write_text(f"{5 - self.rounds_after_special} more rounds for Human's special ability to regenerate\n")

            if self.rounds_after_special == 5:
                self.world.write_text("Human special ability is ready to be used!\n")
                self.rounds_after_special = -1
                self.used_special = False

    def erase_traces(self, h, w):
        self.world.erase_organism(self.position.x, self.position.y)
        self.world.help_animal_move(self, h, w)
        self.position.x = h
        self.position.y = w
        self.world.write_text(f"Human has moved to {self.position.x}, {self.position.y}\n")

    def special_ability(self, h, w):
        if self.used_special:
            return

        dx = [0, 0, 1, 1, 1, -1, -1, -1]
        dy = [1, -1, 0, 1, -1, 0, 1, -1]

        self.world.write_text("Special ability has been used!\n")

        for i in range(8):
            symbol = self.world.return_symbol(h + dx[i], w + dy[i])
            org = None
            if symbol != '?':
                org = self.world.get_organism(h + dx[i], w + dy[i])
            if org:
                self.world.kill_organism(org, h + dx[i], w + dy[i])
                self.world.write_text(f"{org.get_name()} has been killed by Human's special ability!\n")

        self.used_special = True

    def get_rounds_special(self):
        return self.rounds_after_special

    def set_rounds_special(self, rounds):
        self.rounds_after_special = rounds

    def get_used_special(self):
        return self.used_special

    def set_used_special(self, used):
        self.used_special = used
