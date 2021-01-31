class Vertex:

    def __init__(self, identity, y, x):
        self.identity = identity
        self.x = x
        self.y = y
        self.adjacent_vertices = []
        self.value = 0

    def __eq__(self, other):
        if other == self:
            return True
        if not isinstance(other, Vertex):
            return False
        return other.value == self.value

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        if not isinstance(other, Vertex):
            raise Exception(str(other) + ' is not and instance of ' + self.__class__.__name__)
        return other.value < self.value

    def __lt__(self, other):
        if not isinstance(other, Vertex):
            raise Exception(str(other) + ' is not and instance of ' + self.__class__.__name__)
        return other.value > self.value

    def __ge__(self, other):
        if not isinstance(other, Vertex):
            raise Exception(str(other) + ' is not and instance of ' + self.__class__.__name__)
        return other.value <= self.value

    def __le__(self, other):
        if not isinstance(other, Vertex):
            raise Exception(str(other) + ' is not and instance of ' + self.__class__.__name__)
        return other.value >= self.value

    def __str__(self):
        return '[' + str(self.identity) + ', ' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.adjacent_vertices) + ']'
