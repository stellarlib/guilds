from .party_members import Members
from .party_skills import Skills
from .party_inventory import Inventory


class Party(object):

    def __init__(self):

        self.map = None

        self.members = Members(self)
        self.skills = Skills(self)
        self.inventory = Inventory(self)

    # movement
    def move(self, cell):
        self.position(cell)
        self.consume_supplies(cell.map_type)
        cell.trigger(self)

    def position(self, cell):
        # change party position to cell
        pass

    def explore(self, cell):
        self.map.explore(cell)

    def take_damage(self, damage):
        pass

    # inventory
    def consume_supplies(self, cell):
        supplies = self.skills.supply_cost(self.map, cell)
        self.inventory.deplete_supplies(supplies)

    # map pick ups
    def claim_treasure(self):

        silver = self.map.treasure_base + self.map.treasure_bonus_pool * self.skills.treasure_bonus()
        self.inventory.add_silver(int(silver))

    def claim_artifacts(self):

        artifacts = self.map.artifact_base + self.map.artifact_bonus_pool * self.skills.artifact_bonus()
        self.inventory.add_artifacts(artifacts)

    def claim_relics(self):
        relics = self.map.relic_base + self.map.relic_bonus_pool * self.skills.relic_bonus()
        self.inventory.add_relics(relics)

    def claim_ore(self):

        if not self.skills.miner():
            return False

        silver = self.map.ore_base * self.skills.ore_bonus()
        self.inventory.add_silver(silver)

        return True

    def claim_herbs(self):

        if not self.skills.gather_herbs():
            return False

        supplies = self.map.herb_base * self.skills.herb_bonus()
        self.inventory.add_supplies(supplies)

        if self.skills.healing_herbs:
            self.herb_heal()

        return True

    def herb_heal(self):
        pass

    def claim_scrap(self):
        pass

    def hunt_game(self):
        pass

    def trigger_trap(self):
        self.take_damage(self.map.trap_level)

    def detect_cell(self, cell):

        self.skills.detect_cell(cell)
