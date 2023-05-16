import pandas as pd

from lab1 import *
from lab2 import *

#zadanie 1
def generate_random_graph(num_nodes, num_edges):
    if num_edges > num_nodes * (num_nodes - 1) / 2:
        raise ValueError("Number of edges exceeds the maximum possible number of edges.")

    graph = nx.Graph()
    graph.add_nodes_from(range(num_nodes))

    # Generate a connected graph
    for i in range(1, num_nodes):
        node = np.random.choice(i)
        graph.add_edge(i, node)

    # Add remaining edges randomly
    remaining_edges = num_edges - (num_nodes - 1)
    nodes = list(graph.nodes)
    while remaining_edges > 0:
        node1, node2 = np.random.choice(nodes, size=2, replace=False)
        if not graph.has_edge(node1, node2):
            graph.add_edge(node1, node2)
            remaining_edges -= 1

    return graph

def assign_random_edge_weights(graph):
    for u, v in graph.edges:
        weight = np.random.randint(1, 11)
        graph[u][v]['weight'] = weight



# zadanie 2 i zadanie 3

def dijkstra(graph, source):
    # Inicjalizacja
    dist = {node: float('inf') for node in graph.nodes}
    dist[source] = 0
    visited = set()

    # Główna pętla
    while len(visited) < len(graph.nodes):
        # Wybierz wierzchołek z najmniejszą aktualną odległością
        current = min((node for node in graph.nodes if node not in visited), key=lambda node: dist[node])

        # Zaznacz wierzchołek jako odwiedzony
        visited.add(current)

        # Aktualizuj odległości do sąsiadów
        for neighbor in graph.neighbors(current):
            weight = graph[current][neighbor]['weight']
            new_dist = dist[current] + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist

    return dist

def calculate(num_nodes, num_edges, from_node):
    graph = generate_random_graph(num_nodes, num_edges)

    # Przypisywanie losowych wag krawędzi (odległości)
    for u, v in graph.edges:
        weight = np.random.randint(1, 11)
        graph[u][v]['weight'] = weight

    # Wyświetlanie grafu
    nx.draw_circular(graph, with_labels=True, node_color='lightblue')
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos=nx.circular_layout(graph), edge_labels=edge_labels)
    plt.axis('equal')
    plt.show()

    distance_matrix = []
    # Obliczanie najkrótszych ścieżek z wierzchołka 0 do pozostałych wierzchołków
    for main_node in range(num_nodes):
        distances = dijkstra(graph, main_node)
        distance_matrix.append(distances.values())
        for node in distances:
            if from_node == main_node:
                path = nx.shortest_path(graph, main_node, node)
                print(f"Najkrótsza ścieżka od wierzchołka {main_node} do {node}: {path}")
                print(f"Długość ścieżki: {distances[node]}\n")

    return pd.DataFrame(distance_matrix)

# zadanie 4

def calculate_graph_center(adjacency_list, weights):
    num_vertices = len(adjacency_list)
    distances = []
    for vertex in range(num_vertices):
        distances_row = dijkstra(vertex, adjacency_list, weights, num_vertices)
        distances.append(distances_row)
    center = distances.index(min(distances, key=lambda x: sum(x)))
    center_sum = sum(distances[center])
    print(f"The center of the graph is vertex {center} with a total distance of {center_sum}.")
    minimax = distances.index(min(distances, key=lambda x: max(x)))
    minimax_distance = max(distances[minimax])
    print(f"The minimax center of the graph is vertex {minimax} with a distance of {minimax_distance} from the farthest vertex.")



# zadanie 5


# def minimum_spanning_tree_kruskal(graph):
#     mst = nx.Graph()
#     edges = sorted(graph.edges(data=True), key=lambda x: x[2]['weight'])  # Posortowanie krawędzi według wag
#
#     # Inicjalizacja zbiorów rozłącznych
#     subsets = {node: {node} for node in graph.nodes}
#
#     for edge in edges:
#         u, v, weight = edge
#         u_subset = subsets[u]
#         v_subset = subsets[v]
#
#         if u_subset != v_subset:  # Sprawdzenie czy krawędź nie tworzy cyklu
#             mst.add_edge(u, v, weight=weight['weight'])
#             u_subset.update(v_subset)
#
#             for node in v_subset:
#                 subsets[node] = u_subset
#
#     return mst
def minimum_spanning_tree_kruskal(graph):
    mst = nx.Graph()
    edges = sorted(graph.edges(data=True), key=lambda x: x[2]['weight'])  # Posortowanie krawędzi według wag

    # Inicjalizacja zbiorów rozłącznych
    subsets = {node: {node} for node in graph.nodes}

    for edge in edges:
        u, v, weight = edge
        u_subset = subsets[u]
        v_subset = subsets[v]

        if u_subset != v_subset:  # Sprawdzenie czy krawędź nie tworzy cyklu
            mst.add_edge(u, v, weight=weight['weight'])
            u_subset.update(v_subset)

            for node in v_subset:
                subsets[node] = u_subset

    return mst




