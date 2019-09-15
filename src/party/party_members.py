

class Members(object):

    def __init__(self, party):

        self.party = party
        self.roster = []

    @property
    def active_roster(self):
        return filter(lambda hero: hero.active, self.roster)
