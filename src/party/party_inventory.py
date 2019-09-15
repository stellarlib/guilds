

class Inventory(object):

    def __init__(self, party):

        self.party = party

        self.silver = 0
        self.artifacts = 0
        self.relics = 0
        self.supplies = 0

    def add_silver(self, silver):
        self.silver += silver
        # update ui
        # create silver_floater(silver)

    def add_artifacts(self, artifacts):
        self.artifacts += artifacts
        # update ui
        # create artifacts_floater(artifacts)

    def add_relics(self, relics):
        self.relics += relics
        # update ui
        # create relics_floater(relics)

    def add_supplies(self, supplies):
        self.supplies += supplies
        # update ui
        # create supplies_floater(supplies)

    def deplete_supplies(self, supplies):
        self.supplies -= supplies
        # update ui
