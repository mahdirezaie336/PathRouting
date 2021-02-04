from vertex import Vertex


class User:

    path: [Vertex]

    def __init__(self, UID, start_time, start, end):
        self.UID = UID
        self.start_time = start_time
        self.start = start
        self.end = end
        self.path = []
        self.duration_time = float('inf')

    def print(self):
        for i in self.path:
            print(i.identity, end=' ')
        print('Duration time:', self.duration_time)
