from vertex import Vertex


class User:

    path: [Vertex]

    def __init__(self, UID, time, start, end):
        self.UID = UID
        self.time = time
        self.start = start
        self.end = end
        self.path = None
