import os
from abc import ABC, abstractmethod
from tkinter.simpledialog import askstring
import random
from typing import List

from World.Organism.Animal.Wolf import Wolf
from World.Organism.Animal.Sheep import Sheep
from World.Organism.Animal.Turtle import Turtle
from World.Organism.Animal.Fox import Fox
from World.Organism.Animal.Antelope import Antelope
from World.Organism.Animal.CyberSheep import Cybersheep
from World.Organism.Animal.Human import Human
from World.Organism.Plant.Belladonna import Belladonna
from World.Organism.Plant.SowThistle import SowThistle
from World.Organism.Plant.Grass import Grass
from World.Organism.Plant.Guarana import Guarana
from World.Organism.Plant.SosnowskyHogweed import SosnowskyHogweed
from World.Position import Position

ORGANISMS = (
Wolf, Sheep, Turtle, Fox, Antelope, Cybersheep, Human, Belladonna, SowThistle, Grass, Guarana, SosnowskyHogweed)


class World:
    DEFAULT_HEIGHT = 20
    DEFAULT_WIDTH = 20

    def __init__(self, height=DEFAULT_HEIGHT, width=DEFAULT_WIDTH):
        self.height = height
        self.width = width
        self.board = [[None] * width for _ in range(height)]
        self.alive_organisms = []
        self.saved = False
        self.chosen_animal = 'S'

    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    def draw_world(self):
        import os
        os.system("cls")

        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] is None:
                    print(". ", end='')
                else:
                    print(self.board[i][j].get_sign() + " ", end='')
            print()

        self.read_text()

    def count_sos(self):
        counter = 0
        for i in range(self.height):
            for j in range(self.width):
                if self.return_symbol(i, j) == '+':
                    counter += 1
        return counter

    def get_sosnowskys_position(self) -> List[Position]:
        positions = []
        for i in range(self.height):
            for j in range(self.width):
                if self.return_symbol(i, j) == '+':
                    positions.append(Position(i, j))
        return positions

    def get_human_pos(self) -> Position:
        for i in range(self.height):
            for j in range(self.width):
                if self.return_symbol(i, j) == '@':
                    return Position(i, j)
        return Position(99, 99)

    def place_randomly(self, organism):
        pos = self.check_free_position()
        if self.board[pos.x][pos.y] is None:
            organism.set_world(self)
            organism.set_position(pos.x, pos.y)
            self.board[pos.x][pos.y] = organism
            self.alive_organisms.append(organism)

    def check_free_position(self) -> Position:
        positions = [(i, j) for i in range(self.height) for j in range(self.width)]
        random.shuffle(positions)
        for pos_x, pos_y in positions:
            if self.board[pos_x][pos_y] is None:
                return Position(pos_x, pos_y)
        return Position(1, 1)

    def start_game(self):
        sheep = Sheep()
        sheep2 = Sheep()

        wolf = Wolf()
        wolf2 = Wolf()
        wolf3 = Wolf()
        wolf4 = Wolf()

        turtle = Turtle()
        turtle2 = Turtle()

        antelope = Antelope()

        human = Human(self, Position(3, 3))

        fox = Fox()
        fox2 = Fox()

        belladonna = Belladonna()

        grass = Grass()
        grass2 = Grass()

        sow = SowThistle()

        guarana = Guarana()
        guarana2 = Guarana()

        sos = SosnowskyHogweed()
        sos2 = SosnowskyHogweed()
        sos3 = SosnowskyHogweed()

        cybersheep = Cybersheep()
        cybersheep2 = Cybersheep()

        self.place_randomly(human)
        self.place_randomly(cybersheep)
        self.place_randomly(cybersheep2)

        self.place_randomly(sheep)
        self.place_randomly(sheep2)

        self.place_randomly(wolf)
        self.place_randomly(wolf2)
        self.place_randomly(wolf3)
        self.place_randomly(wolf4)

        self.place_randomly(turtle)
        self.place_randomly(turtle2)

        self.place_randomly(antelope)

        self.place_randomly(fox)
        self.place_randomly(fox2)

        self.place_randomly(belladonna)

        self.place_randomly(grass)
        self.place_randomly(grass2)

        self.place_randomly(sow)

        self.place_randomly(guarana)
        self.place_randomly(guarana2)

        self.place_randomly(sos)
        self.place_randomly(sos2)
        self.place_randomly(sos3)

        self.reset_text()

    def add_organism_to_board(self, pos_x, pos_y, sign):
        organism = None

        if sign == 'W':
            organism = Wolf()
        elif sign == 'A':
            organism = Antelope()
        elif sign == 'b':
            organism = Belladonna()
        elif sign == 'F':
            organism = Fox()
        elif sign == 'g':
            organism = Grass()
        elif sign == 'G':
            organism = Guarana()
        elif sign == 'S':
            organism = Sheep()
        elif sign == '+':
            organism = SosnowskyHogweed()
        elif sign == 's':
            organism = SowThistle()
        elif sign == 'T':
            organism = Turtle()
        elif sign == '@':
            organism = Human()

        if organism:
            organism.set_world(self)
            organism.set_position(pos_x, pos_y)
            self.board[pos_x][pos_y] = organism
            self.alive_organisms.append(organism)

    def make_turn(self):
        if self.check_end_game():
            self.end_game()

        original_length = len(self.alive_organisms)

        for i in range(original_length - 1):
            org = self.alive_organisms[i]

            if org.get_moved():
                continue

            max_index = i

            for j in range(i + 1, len(self.alive_organisms)):
                current_org = self.alive_organisms[j]

                if current_org.get_moved():
                    continue

                if current_org.get_sign() == '@':
                    current_org.set_moved(True)

                if (current_org.get_initiative() > self.alive_organisms[max_index].get_initiative() or
                        (current_org.get_initiative() == self.alive_organisms[max_index].get_initiative() and
                         current_org.get_years() > self.alive_organisms[max_index].get_years())):
                    max_index = j

            if max_index != i:
                self.alive_organisms[i], self.alive_organisms[max_index] = self.alive_organisms[max_index], self.alive_organisms[i]

            if org.get_sign() != '@':
                org.action()

            org.set_moved(True)
            original_length = len(self.alive_organisms)

        for org in self.alive_organisms:
            org.set_moved(False)

        self.read_text()

        if self.saved:
            self.save_game_status()
            self.saved = False
            self.write_text("Game state saved!\n")
            return

    def set_saved(self, save):
        self.saved = save

    def return_saved(self):
        return self.saved

    def erase_organism(self, pos_x, pos_y):
        self.board[pos_x][pos_y] = None

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_chosen_animal(self):
        return self.chosen_animal

    def set_chosen_animal(self, chosen):
        self.chosen_animal = chosen

    def return_symbol(self, h, w):
        if 0 <= h < self.height and 0 <= w < self.width:
            if self.board[h][w] is None:
                return '*'
            else:
                return self.board[h][w].get_sign()
        else:
            return '?'

    def get_organism(self, h, w):
        return self.board[h][w]

    def kill_organism(self, organism, h, w):
        self.erase_organism(h, w)
        self.alive_organisms.remove(organism)

    def write_text(self, text):
        with open("Log.txt", "a") as writer:
            writer.write(text)

    def read_text(self):
        print("=-=-=-=-=-= NEXT ROUND =-=-=-=-=-=")
        try:
            with open("Log.txt", "r") as file:
                for line in file:
                    print(line, end='')
        except FileNotFoundError:
            return

        self.reset_text()

    def reset_text(self):
        open("Log.txt", "w").close()

    def end_game(self):
        self.end_text()
        os._exit(0)

    def end_text(self):
        self.reset_text()
        self.write_text("Game Over - Human died!\n")

    def check_end_game(self):
        for organism in self.alive_organisms:
            if organism.get_name() == "Human":
                return False
        return True

    def help_animal_move(self, organism, h, w):
        organism.set_world(self)
        organism.set_position(h, w)
        self.board[h][w] = organism

    def save_game_status(self):
        try:
            with open("game.txt", "w") as file:
                file.write(f"{self.get_height()} {self.get_width()}\n")
                file.write(f"{len(self.alive_organisms)}\n")

                for organism in self.alive_organisms:
                    position = organism.get_position()
                    file.write(f"{organism.get_sign()} {position.x} {position.y} ")
                    file.write(f"{organism.get_strength()} {organism.get_initiative()} {organism.get_years()} ")

                    if organism.get_sign() == '@':
                        file.write(f"{organism.get_rounds_special()} ")
                        file.write(f"{organism.get_used_special()}")

                    file.write("\n")

            print("Game state saved")

        except IOError as e:
            print(e)

    def load_game_status(self):
        try:
            with open("game.txt", "r") as file:
                height, width = map(int, file.readline().split())
                num_organisms = int(file.readline().strip())

                self.board = [[None for _ in range(width)] for _ in range(height)]
                self.height = height
                self.width = width
                self.alive_organisms.clear()

                for i in range(self.height):
                    for j in range(self.width):
                        self.erase_organism(i, j)

                for _ in range(num_organisms):
                    data = file.readline().split()
                    symbol = data[0]
                    x, y = int(data[1]), int(data[2])
                    strength, initiative, year = int(data[3]), int(data[4]), int(data[5])

                    if symbol == '@':
                        rounds_special = int(data[6])
                        used_special = bool(data[7])
                        new_org = Human(self, Position(x, y))
                        new_org.set_rounds_special(rounds_special)
                        new_org.set_used_special(used_special)
                    elif symbol == 'W':
                        new_org = Wolf(self, Position(x, y))
                    elif symbol == 'A':
                        new_org = Antelope(self, Position(x, y))
                    elif symbol == 'b':
                        new_org = Belladonna(self, Position(x, y))
                    elif symbol == 'F':
                        new_org = Fox(self, Position(x, y))
                    elif symbol == 'g':
                        new_org = Grass(self, Position(x, y))
                    elif symbol == 'G':
                        new_org = Guarana(self, Position(x, y))
                    elif symbol == 'S':
                        new_org = Sheep(self, Position(x, y))
                    elif symbol == '+':
                        new_org = SosnowskyHogweed(self, Position(x, y))
                    elif symbol == 's':
                        new_org = SowThistle(self, Position(x, y))
                    elif symbol == 'T':
                        new_org = Turtle(self, Position(x, y))
                    elif symbol == 'C':
                        new_org = Cybersheep(self, Position(x, y))
                    else:
                        continue

                    new_org.set_strength(strength)
                    new_org.set_initiative(initiative)
                    new_org.set_years(year)
                    new_org.set_moved(False)
                    self.help_animal_move(new_org, x, y)
                    self.alive_organisms.append(new_org)

            print("Game state loaded")

        except IOError:
            print("Error. Could not open the file")
