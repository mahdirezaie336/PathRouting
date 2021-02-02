from heap_utils import MinHeap
from vertex import *
from edge import Edge
from copy import deepcopy


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

heapq.heapify(graph)
for i in graph:
    print(i)

vertices = deepcopy(graph)
# Getting commands
while True:
    hash_table = {i.identity: i for i in vertices}
    for i in vertices:
        i.value = float('inf')
        i.prev = None

    break
