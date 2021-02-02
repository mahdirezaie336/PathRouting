class MinHeap:

    def __init__(self, array=[], index_table={}):
        self.array = array
        self.index_table = index_table
        self.make_heap()

    def make_heap(self):
        for i in range(len(self.array) // 2).__reversed__():
            self.min_heapify(i)
        for index, vertex in enumerate(self.array):
            self.index_table[vertex.identity] = index

    def add(self, vertex):
        index = len(self.array)
        self.array.append(vertex)
        self.min_up_heapify(index)
        self.index_table[vertex.identity] = index

    def remove(self, vertex_id):
        index = self.index_table[vertex_id]
        last_item = self.array[-1]
        self.index_table[last_item] = index
        del self.array[-1]
        self.array[index] = last_item
        self.min_heapify(index)
        self.min_up_heapify(index)

    def min_heapify(self, i):
        # Makes a heap when the item with index i has a right and left
        # subtrees which both are heaps.
        le = self.left(i)
        ri = self.right(i)
        smallest = self.minimum(le, ri, i)
        if smallest != i:
            self.swap(i, smallest)
            self.min_heapify(smallest)

    def min_up_heapify(self, i):
        pa = self.parent(i)
        smallest = self.minimum(pa, i)
        if smallest != pa:
            self.swap(i, smallest)
            self.min_up_heapify(smallest)

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

    def parent(self, i):
        pa = (i - 1) // 2
        if pa < 0 or len(self.array) == 0:
            return 0
        return pa

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
