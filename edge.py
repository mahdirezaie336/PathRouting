from vertex import Vertex


class Edge:

    head: Vertex
    tail: Vertex

    def __init__(self, head, tail):
        self.head = head
        self.tail = tail
        self.weight = 0

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
