from heap_hashtable import MinHeap
from vertex import *
from edge import Edge
from copy import deepcopy
from constants import Constants
from user import User
import heapq
import time


users = []


def get_vertex(Id):
    for i in graph:
        if i.identity == Id:
            return i
    raise Exception('From routing program: Vertex not found!')


# Reading map file
with open(Constants.map_path, 'r') as map_file:
    n, m = [int(i) for i in map_file.readline().split()]
    graph = [Vertex(0, 0, 0)] * n
    roads = {}

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
        edge = Edge(get_vertex(id1), get_vertex(id2))
        roads[id1, id2] = edge
        roads[id2, id1] = edge


while True:
    vertices = deepcopy(graph)
    edges = deepcopy(roads)
    heap = MinHeap(vertices)

    print('Enter "time start_id end_id": ', end=' ')
    time, start_id, end_id = [float(i) for i in input().split()]
    start_id = int(start_id)
    end_id = int(end_id)
    users.append(User(len(users), time, start_id, end_id))

    # Putting each user on their ways
    for user in range(len(users) - 1):
        edge_to_put = None
        user_time = user.time
        # Moving on user path
        for i in range(len(user.path) - 1):
            id1 = user.path[i].identity
            id2 = user.path[i + 1].identity
            edge = edges[id1, id2]
            if user_time <= edge.get_weight() * 120:
                edge_to_put = edge
                break
            user_time -= edge.get_weight()
        if edge_to_put is not None:
            edge_to_put.users.append(user)

    # Finding best way for the last user using Dijkstra algorithm
    heap.modify(start_id, 0)
    last_node = None
    while end_id in heap:
        current = heap.pop()
        for neighbour_id in current.adjacent_vertices:
            if neighbour_id not in heap:
                continue
            neighbour = heap.get_vertex(neighbour_id)
            edge_weight = edges[current.identity, neighbour_id].get_weight()
            if current.value + edge_weight < neighbour.value:
                heap.modify(neighbour_id, edge_weight + current.value)
                neighbour.prev = current
        last_node = current

    def set_user_path(vertex):
        if vertex.prev is not None:
            set_user_path(vertex.prev)
        users[-1].path.append(vertex)

    set_user_path(last_node)
    users[-1].duration_time = last_node.value
    users[-1].print()
