from vertex import Vertex
from constants import Constants


class Edge:

    head: Vertex
    tail: Vertex

    def __init__(self, head, tail):
        self.head = head
        self.tail = tail
        self.weight = 0
        self.users = []

    def get_weight(self):
        x1 = self.head.x
        x2 = self.tail.x
        y1 = self.head.y
        y2 = self.tail.y
        length = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
        return length * (1 + Constants.traffic_factor * len(self.users))

    def __eq__(self, other):
        if other == self:
            return True
        if not isinstance(other, Edge):
            return False
        return other.weight == self.weight

    def __hash__(self) -> int:
        return hash(self.weight)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        if not isinstance(other, Edge):
            raise Exception(str(other) + ' is not and instance of ' + self.__class__.__name__)
        return other.weight < self.weight

    def __lt__(self, other):
        if not isinstance(other, Edge):
            raise Exception(str(other) + ' is not and instance of ' + self.__class__.__name__)
        return other.weight > self.weight

    def __ge__(self, other):
        if not isinstance(other, Edge):
            raise Exception(str(other) + ' is not and instance of ' + self.__class__.__name__)
        return other.weight <= self.weight

    def __le__(self, other):
        if not isinstance(other, Edge):
            raise Exception(str(other) + ' is not and instance of ' + self.__class__.__name__)
        return other.weight >= self.weight

    def __str__(self):
        return 'Head: ' + str(self.head) + ' Tail: ' + str(self.tail)
