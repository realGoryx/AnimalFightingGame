from World.Organism.Animal.Animal import Animal


class Wolf(Animal):
    def __init__(self, world=None, pos=None):
        super().__init__()
        self.strength = 9
        self.initiative = 5
        self.set_sign('W')
        self.set_name("Wolf")
        self.set_world(world)
        if world and pos:
            self.set_position(pos.x, pos.y)
            self.set_position(pos.x, pos.y)
