from World.Organism.Animal.Animal import Animal


class Sheep(Animal):
    def __init__(self, world=None, pos=None):
        super().__init__()
        self.strength = 4
        self.initiative = 4
        self.set_sign('S')
        self.set_name("Sheep")
        if world and pos:
            self.set_world(world)
            self.set_position(pos.x, pos.y)