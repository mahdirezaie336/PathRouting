class Vertex:

    def __init__(self, identity, y, x):
        self.identity = identity
        self.x = x
        self.y = y
        self.adjacent_vertices = []

    def __str__(self):
        return '[' + str(self.identity) + ', ' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.adjacent_vertices) + ']'
