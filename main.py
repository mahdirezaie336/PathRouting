from heap_hashtable import MinHeap
from vertex import *
from edge import Edge
from copy import deepcopy
import heapq


map_path = './map.txt'


def get_vertex(Id):
    for i in graph:
        if i.identity == Id:
            return i
    raise Exception('From routing program: Vertex not found!')


# Reading map file
with open(map_path, 'r') as map_file:
    n, m = [int(i) for i in map_file.readline().split()]
    graph = [Vertex(0, 0, 0)] * n

    # Reading vertices
    for i in range(n):
        identity, y, x = (float(i) for i in map_file.readline().split())
        identity = int(identity)
        graph[i] = Vertex(identity, y, x)

    # Reading edges
    for i in range(m):
        id1, id2 = (int(i) for i in map_file.readline().split())
        get_vertex(id1).adjacent_vertices.append(id2)
        get_vertex(id2).adjacent_vertices.append(id1)

sizes = [100, 250, 1, 3, 2, 6]
for i, value in enumerate(sizes):
    graph[i].value = value

heap = MinHeap(deepcopy(graph))
vv = Vertex(45, 1.0011, 1.0011, 0)
heap.add(vv)
for i in heap.array:
    print(i)
print('Dictionary of heap is:', heap.index_table)

heapq.heapify(sizes)
print('Sizes after heapify is:', sizes)
