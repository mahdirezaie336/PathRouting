import heapq
from vertex import *
from edge import Edge


map_path = './map.txt'
graph = []


def get_vertex(Id):
    for i in graph:
        if i.identity == Id:
            return i
        raise Exception('From rounting program: Vertex not found!')


# Reading map file
with open(map_path, 'r') as map_file:
    n, m = map_file.readline().split()
    graph = [0]*n

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



