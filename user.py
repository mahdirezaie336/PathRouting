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
        self.remain_time = 0

    def print(self):
        for i in self.path:
            print(i.identity, end=' ')
        print()
        print(self.duration_time)

    def __str__(self):
        return 'UID: ' + str(self.UID)

    def __repr__(self):
        return 'UID: ' + str(self.UID) + ' remain time: ' + str(self.remain_time)
