from abc import ABC, abstractmethod
from World.Position import Position


class Organism:
    def __init__(self, strength=0, initiative=0, pos=None, world=None):
        self.strength = strength
        self.initiative = initiative
        self.movement_speed = 0
        self.years_old = 0
        self.position = pos if pos else Position()
        self.sign = ''
        self.name = ''
        self.world = world
        self.moved_flag = False

    def action(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def collision(self, attacking):
        raise NotImplementedError("Subclass must implement abstract method")

    def special_attack(self, attack, defend):
        return False

    def get_sign(self):
        return self.sign

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_strength(self):
        return self.strength

    def set_strength(self, strength):
        self.strength = strength

    def get_initiative(self):
        return self.initiative

    def set_initiative(self, initiative):
        self.initiative = initiative

    def set_sign(self, sign):
        self.sign = sign

    def set_world(self, world):
        self.world = world

    def get_position(self):
        return self.position

    def set_position(self, x, y):
        self.position.set_x(x)
        self.position.set_y(y)

    def get_years(self):
        return self.years_old

    def set_years(self, years_old):
        self.years_old = years_old

    def get_moved(self):
        return self.moved_flag

    def set_moved(self, moved_flag):
        self.moved_flag = moved_flag

    def get_movement_speed(self):
        return self.movement_speed

    def set_movement_speed(self, movement_speed):
        self.movement_speed = movement_speed