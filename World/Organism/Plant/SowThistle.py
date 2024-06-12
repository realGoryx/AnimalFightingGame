from World.Organism.Plant.Plant import Plant


class SowThistle(Plant):
    def __init__(self, world=None, pos=None):
        super().__init__()
        self.strength = 0
        self.initiative = 0
        self.set_sign('s')
        self.set_name("Sow Thistle")
        if world and pos:
            self.set_position(pos.x, pos.y)
            self.set_position(pos.x, pos.y)

    def action(self):
        self.set_years(self.get_years() - 2)

        for i in range(3):
            super().action()
