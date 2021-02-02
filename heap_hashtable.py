class MinHeap:

    def __init__(self, array=[], index_table={}):
        self.array = array
        self.index_table = index_table
        self.make_heap()

    def make_heap(self):
        for i in range(len(self.array) // 2 - 1, -1, -1):
            self.min_heapify(i)
        for index, vertex in enumerate(self.array):
            self.index_table[vertex.identity] = index

    def min_heapify(self, i):
        # Makes a heap when the item with index i has a right and left
        # subtrees which both are heaps.
        le = self.left(i)
        ri = self.right(i)
        largest = self.minimum(le, ri, i)
        if largest != i:
            self.swap(i, largest)
            self.min_heapify(largest)

    def right(self, i):
        ri = 2 * i + 2
        if ri < len(self.array):
            return ri
        return i

    def left(self, i):
        ri = 2 * i + 1
        if ri < len(self.array):
            return ri
        return i

    @staticmethod
    def parent(i):
        return (i - 1) // 2

    def swap(self, i, j):
        temp = self.array[i]
        self.array[i] = self.array[j]
        self.array[j] = temp

    def minimum(self, *index):
        smallest = index[0]
        for i in index:
            if i < len(self.array):
                if self.array[i] < self.array[smallest]:
                    smallest = i
        return smallest

    def __str__(self):
        return self.array.__str__()
