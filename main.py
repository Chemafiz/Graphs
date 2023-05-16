from lab1 import *
from lab2 import *
from lab3 import *
import random
#LAB1-------------------------------------------------------------------------
# data = load_data(r"data\test1.csv")
# draw_graph(data, 3)
#
# data = make_random_graph(10, p=0.87)
# draw_graph(data, 1)
# save_data(data, "output")

#LAB2--------------------------------------------------------------------------
#zad1
# graph = construct_graph([2, 2, 3, 2, 1, 4, 2, 2, 2, 6,0, 0, 0])
# draw_graph(graph, 1)
#
# #zad2
# graph = randomize_graph(graph, 10)
# draw_graph(graph, 1)
#
# #zad3
# all_compononts = all_connected_components(graph)
# draw_graph(graph, 1, groups=all_compononts)

#zad4
# graph = generate_eulerian_graph(50)
# draw_graph(graph, 1)
# eulerian_cycle = find_eulerian_cycle(graph)
# print(eulerian_cycle)

# zad5
# graph = generate_k_regular_graph(6, 2)
# draw_graph(graph, 2)
#
# #zad6
# print(is_hamiltonian(graph))


#LAB 3--------------------------------------------------------------------
#zad1
# Generate a random graph with 10 nodes and 15 edges
# graph = generate_random_graph(5, 6)
#
# # Assign random weights to the edges
# assign_random_edge_weights(graph)
#
# # Draw the graph
# draw_graph(nx.to_numpy_array(graph), module=1, labels=True)


#zad2 i zad3
# df = calculate(10,15, 6)
# print(df)
#
# # zad4
# # print(df.sum())
# centrum = df.sum().idxmin()
# print(f"Centrum grafu to wierzchołek {centrum} z odległością {df.sum()[centrum]}")
# print(f"Centrum minimax grafu to wierzchołek {df.max().idxmin()}")

#zad5
# graph = generate_random_graph(10, 15)
#
# # Assign random weights to the edges
# assign_random_edge_weights(graph)
#
# # Draw the graph
# draw_graph(nx.to_numpy_array(graph), module=1, labels=True)
#
# # Wywołanie funkcji minimum_spanning_tree_kruskal
# mst = minimum_spanning_tree_kruskal(graph)
#
# # Wyświetlanie minimalnego drzewa rozpinającego
# nx.draw_circular(mst, with_labels=True, node_color='lightblue')
# edge_labels = nx.get_edge_attributes(mst, 'weight')
# nx.draw_networkx_edge_labels(mst, pos=nx.circular_layout(mst), edge_labels=edge_labels)
# plt.axis('equal')
# plt.show()

graph = generate_random_graph(10, 15)

# Assign random weights to the edges
assign_random_edge_weights(graph)

# Draw the graph
draw_graph(nx.to_numpy_array(graph), module=1, labels=True)

# Wywołanie funkcji minimum_spanning_tree_kruskal
mst = minimum_spanning_tree_kruskal(graph)

# Wyświetlanie minimalnego drzewa rozpinającego
nx.draw_circular(mst, with_labels=True, node_color='lightblue')
edge_labels = nx.get_edge_attributes(mst, 'weight')
nx.draw_networkx_edge_labels(mst, pos=nx.circular_layout(mst), edge_labels=edge_labels)
plt.axis('equal')
plt.show()


