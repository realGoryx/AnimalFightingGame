from World.Organism.Plant.Plant import Plant
from World.Organism.Animal.Animal import Animal


class Guarana(Plant):
    def __init__(self, world=None, pos=None):
        super().__init__()
        self.strength = 0
        self.initiative = 0
        self.sign = 'G'
        self.name = "Guarana"
        if world and pos:
            self.set_position(pos.x, pos.y)
            self.set_position(pos.x, pos.y)

    def special_attack(self, attack, defend):
        if self == defend:
            attacker_strength = attack.get_strength()
            attack.set_strength(attacker_strength + 3)
            self.world.kill_organism(self, self.get_position().get_x(), self.get_position().get_y())
            self.world.write_text(attack.get_name() + "'s strength has been increased by 3!\n")
            return True
        return False