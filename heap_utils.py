class MinHeap:

    def __init__(self, array=[]):
        self.array = array
        MinHeap.make_heap(array)

    @staticmethod
    def make_heap(array):
        for i in range(len(array) // 2 - 1, 0):
            MinHeap.min_heapify(array, i)

    @staticmethod
    def min_heapify(heap, i):
        # Makes a heap when the item with index i has a right and left
        # subtrees which both are heaps.
        le = MinHeap.left(i)
        ri = MinHeap.right(i)
        largest = max(le, ri, i)
        if largest != i:
            MinHeap.swap(heap, i, largest)
            MinHeap.min_heapify(heap, largest)

    @staticmethod
    def right(i):
        return 2 * i + 2

    @staticmethod
    def left(i):
        return 2 * i + 1

    @staticmethod
    def parent(i):
        return (i - 1) // 2

    @staticmethod
    def swap(A, i, j):
        temp = A[i]
        A[i] = A[j]
        A[j] = temp
