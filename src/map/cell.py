from .map_coord import MapCoord


class Cell(object):

    def __init__(self, map, terrain, coord):

        self.map = map
        self.terrain = terrain
        self.coord = MapCoord(coord)
        self.links = []
        self.contents = 'none'
        self.explored = False
        self.contents_hidden = True
        self.foe = None

        self._trigger = {
            'treasure': self.find_treasure,
            'trap': self.trigger_trap,
            'ore': self.find_ore,
            'relic': self.find_relics,
            'artifact': self.find_artifacts,
            'herb': self.find_herbs,
            'scrap': self.find_scrap,
            'game': self.find_game,
            'foe': self.battle_foes,
            'none': self.find_nothing,
        }

    @property
    def empty(self):
        return self.contents == 'none'

    def link_to_adj(self):
        for coord in self.coord.get_adj():
            cell = self.map.get_cell(coord)
            if cell:
                self.links.append(cell)

    def discover(self):
        self.contents_hidden = False
        # update display

    def clear(self):
        self.contents = 'none'
        self.explored = True
        self.contents_hidden = False

    def trigger(self, party):
        self._trigger[self.contents](party)

    def disarm_trap(self):
        self.clear()

    # trigger functions
    def find_nothing(self, party):
        pass

    def find_treasure(self, party):
        party.claim_treasure()
        self.clear()

    def find_ore(self, party):
        party.claim_ore()
        self.clear()

    def find_artifacts(self, party):
        party.claim_artifacts()
        self.clear()

    def find_relics(self, party):
        party.claim_relics()
        self.clear()

    def find_herbs(self, party):
        claimed = party.claim_herbs()
        if claimed:
            self.clear()

    def find_game(self, party):
        party.hunt_game()
        self.clear()

    def find_scrap(self, party):
        party.claim_scrap()
        self.clear()

    def trigger_trap(self, party):
        party.trigger_trap()
        self.clear()

    def battle_foes(self, party):
        pass
