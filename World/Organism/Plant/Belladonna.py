from World.Organism.Plant.Plant import Plant


class Belladonna(Plant):
    def __init__(self, world=None, pos=None):
        super().__init__()
        self.strength = 99
        self.initiative = 0
        self.sign = 'b'
        self.name = "Belladonna"
        if world and pos:
            self.set_position(pos.x, pos.y)
            self.set_position(pos.x, pos.y)

    def special_attack(self, attack, defend):
        if self == defend:
            self.world.kill_organism(attack, attack.get_position().get_x(), attack.get_position().get_y())
            self.world.write_text("Belladonna has poisoned and killed " + attack.get_name() + "!\n")
            return True
        return False
