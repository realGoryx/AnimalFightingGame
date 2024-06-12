from World.Organism.Plant.Plant import Plant


class Grass(Plant):
    def __init__(self, world=None, pos=None):
        super().__init__()
        self.strength = 0
        self.initiative = 0
        self.sign = 'g'
        self.name = "Grass"
        if world and pos:
            self.set_position(pos.x, pos.y)
            self.set_position(pos.x, pos.y)

    def action(self):
        pass

    def collision(self, attacking):
        pass