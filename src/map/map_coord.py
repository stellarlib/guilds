

class MapCoord(object):

    def __init__(self, coord):

        self.x, self.y = coord
        self.coord = coord

    def get_adj(self):

        return [(self.x, self.y-1), (self.x+1, self.y),
                (self.x, self.y+1), (self.x-1, self.y)]
