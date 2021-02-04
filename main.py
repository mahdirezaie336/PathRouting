from heap_hashtable import MinHeap
from vertex import *
from edge import Edge
from copy import deepcopy
from constants import Constants
from user import User
import matplotlib.pyplot as plt


users = []
graph = []
verts = {}
roads = {}


def get_vertex(Id):
    return verts[Id]


# Reading map file
with open(Constants.map_path, 'r') as map_file:
    n, m = [int(i) for i in map_file.readline().split()]

    # Reading vertices
    for i in range(n):
        identity, y, x = (float(i) for i in map_file.readline().split())
        identity = int(identity)
        vertex = Vertex(identity, y, x)
        graph.append(vertex)
        verts[identity] = vertex

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
    for user in users:
        if user == users[-1]:
            continue
        edge_to_put = None
        user_time = time
        # Moving on user path
        for i in range(len(user.path) - 1):
            id1 = user.path[i].identity
            id2 = user.path[i + 1].identity
            edge = edges[id1, id2]
            if user_time <= edge.get_weight() * 120:
                edge_to_put = edge
                break
            user_time -= edge.get_weight() * 120
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

    # Recursive function to get path
    def set_user_path(node):
        if node.prev is not None:
            set_user_path(node.prev)
        users[-1].path.append(node)

    # Add change user path
    set_user_path(last_node)
    users[-1].duration_time = last_node.value * 120
    users[-1].print()

    # Change plot background color
    fig, ax = plt.subplots(nrows=1, ncols=1)
    fig.set_facecolor('#f2efe9')

    # Plotting whole graph
    odd = True
    for e in edges:
        if odd:
            x1 = edges[e].head.x
            x2 = edges[e].tail.x
            y1 = edges[e].head.y
            y2 = edges[e].tail.y
            plt.plot([x1, x2], [y1, y2], marker='o', color='#d8d8d8',
                     markerfacecolor='#1f77b4', markersize=5, markeredgewidth=0)
            plt.annotate(str(edges[e].head.identity), (x1, y1), fontsize=8)
            plt.annotate(str(edges[e].tail.identity), (x2, y2), fontsize=8)
        odd = not odd

    # Plotting path for user
    for i in range(len(users[-1].path) - 1):
        x1 = users[-1].path[i].x
        y1 = users[-1].path[i].y
        x2 = users[-1].path[i + 1].x
        y2 = users[-1].path[i + 1].y
        plt.plot([x1, x2], [y1, y2], marker='o', color='#f8530c')

    plt.show()
