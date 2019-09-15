

class Map(object):

    def __init__(self):

        self.cells = []
        self.level = 1

    def artifact_bonus(self):
        return self.level
