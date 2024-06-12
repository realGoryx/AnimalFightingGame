import random
import time
import tkinter as tk

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
from World.World import World

WORLD_HEIGHT = 12
WORLD_WIDTH = 12

CELL_SIZE = 50


class GameApp:
    def __init__(self, root):
        self.root = root
        self.world = World(WORLD_HEIGHT, WORLD_WIDTH)
        self.canvas = tk.Canvas(root, width=WORLD_WIDTH * CELL_SIZE, height=WORLD_HEIGHT * CELL_SIZE)
        self.canvas.pack()

        self.images = {
            '.': tk.PhotoImage(file="Images/Blank.png"),
            'W': tk.PhotoImage(file="Images/Wolf.png"),
            'S': tk.PhotoImage(file="Images/Sheep.png"),
            'T': tk.PhotoImage(file="Images/Turtle.png"),
            'F': tk.PhotoImage(file="Images/Xardas.png"),
            'A': tk.PhotoImage(file="Images/Antelope.png"),
            'C': tk.PhotoImage(file="Images/Cybersheep.png"),
            '@': tk.PhotoImage(file="Images/Bezi.png"),
            'b': tk.PhotoImage(file="Images/Belladonna.png"),
            's': tk.PhotoImage(file="Images/Sow.png"),
            'g': tk.PhotoImage(file="Images/Grass.png"),
            'G': tk.PhotoImage(file="Images/Dragon.png"),
            '+': tk.PhotoImage(file="Images/Sosnowsky.png")
        }

        self.start_game()
        self.update_canvas()

        self.root.bind("<Up>", self.on_arrow_key)
        self.root.bind("<Down>", self.on_arrow_key)
        self.root.bind("<Left>", self.on_arrow_key)
        self.root.bind("<Right>", self.on_arrow_key)
        self.root.bind("e", self.on_arrow_key)
        self.root.bind("s", self.on_arrow_key)
        self.root.bind("l", self.on_arrow_key)

    def start_game(self):
        print("+-------------------------+")
        print("|  Animal fighting game   |")
        print("|                         |")
        print("|                         |")
        print("|    1 - New Game         |")
        print("|    2 - Load Game        |")
        print("|                         |")
        print("+-------------------------+")
        key = input()

        if key == '1':
            self.world.start_game()
        elif key == '2':
            self.world.load_game_status()
        self.update_canvas()

    def update_canvas(self):
        self.canvas.delete("all")
        for i in range(self.world.height):
            for j in range(self.world.width):
                organism = self.world.board[i][j]
                if organism is None:
                    img = self.images['.']
                else:
                    img = self.images[organism.get_sign()]
                self.canvas.create_image(j * CELL_SIZE, i * CELL_SIZE, anchor=tk.NW, image=img)
        self.root.after(100, self.update_world)

    def update_world(self):
        #self.world.make_turn()
        self.update_canvas()

    def on_arrow_key(self, event):
        next_round = True

        humanPos = self.world.get_human_pos()
        humanX = humanPos.get_x()
        humanY = humanPos.get_y()

        if humanX == 99 and humanY == 99:
            self.root.quit()

        organism = self.world.get_organism(humanX, humanY)
        if isinstance(organism, Human):
            human = organism

        if event.keysym == 'Up':
            human.move_up()
        elif event.keysym == 'Down':
            human.move_down()
        elif event.keysym == 'Left':
            human.move_left()
        elif event.keysym == 'Right':
            human.move_right()
        elif event.keysym == 'e':
            print("e key pressed")
            if not human.used_special:
                human.special_ability(humanX, humanY)
        elif event.keysym == 's':
            self.world.set_saved(True)
            print("Game has been saved!")
            next_round = False
        elif event.keysym == 'l':
            self.world.load_game_status()
            print("Game has been loaded")
            next_round = False

        if next_round:
            self.world.make_turn()


def main():
    root = tk.Tk()
    root.title("Animal Fighting Game Szymon Rozycki")
    root.geometry(f"{WORLD_WIDTH * CELL_SIZE}x{WORLD_HEIGHT * CELL_SIZE}")
    app = GameApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
