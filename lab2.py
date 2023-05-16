from lab1 import *


def is_graphic_sequence(seq):
    seq = np.sort(seq)[::-1]
    while seq[0] > 0:
        if seq[0] >= len(seq):
            return False
        seq[1:seq[0] + 1] -= 1
        if np.any(seq[1:seq[0] + 1] < 0):
            return False
        seq = np.sort(seq[1:])[::-1]
    return True


def construct_graph(seq):
    if is_graphic_sequence(seq):
        n = len(seq)
        graph = np.zeros((n, n), dtype=int)
        seq = np.sort(seq)[::-1]
        for i in range(n):
            for j in range(i + 1, n):
                if seq[i] > 0 and seq[j] > 0:
                    graph[i, j] = 1
                    graph[j, i] = 1
                    seq[i] -= 1
                    seq[j] -= 1
        return graph
    else:
        return None


# zadanie 2 do naprawienia


def random_edge_swap(graph):
    n = graph.shape[0]
    # losowo wybieramy 2 pary krawędzi
    a, b, c, d = random.sample(range(n), 4)
    while b == a or c == d or graph[a, b] == 0 or graph[c, d] == 0 or graph[a, d] == 1 or graph[b, c] == 1:
        a, b, c, d = random.sample(range(n), 4)
    # zamieniamy krawędzie
    graph[a, b] = 0
    graph[b, a] = 0
    graph[c, d] = 0
    graph[d, c] = 0
    graph[a, d] = 1
    graph[d, a] = 1
    graph[b, c] = 1
    graph[c, b] = 1
    return graph


# # funkcja randomizująca graf
def randomize_graph(graph, num_iterations):
    for i in range(num_iterations):
        graph = random_edge_swap(graph)
    return graph


def randomize_edges(neighbourList, number, verbose=False):
    edges = []
    numberOfEdges = 0
    for index, neighbours in enumerate(neighbourList):
        edges.extend((index, neighbour) for neighbour in neighbours)
        numberOfEdges += len(neighbours)
    if numberOfEdges == 0:
        return edges
    i = 0
    while i < number:
        randAB = np.random.randint(0, numberOfEdges)
        randCD = randAB
        while randCD == randAB:
            randCD = np.random.randint(0, numberOfEdges)

        if verbose:
            print(f"{edges[randAB]}, {edges[randCD]} => ", end="")

        AB = list(edges[randAB])
        CD = list(edges[randCD])
        AB[0], AB[1], CD[0], CD[1] = AB[0], CD[1], AB[1], CD[0]

        reversed = AB[::-1]
        if (
            tuple(AB) not in edges
            and tuple(reversed) not in edges
            and tuple(CD) not in edges
            and tuple(CD[::-1]) not in edges
            and AB[0] != AB[1]
            and CD[0] != CD[1]
            and AB != CD
        ):
            edges[randAB], edges[randCD] = tuple(AB), tuple(CD)
            if verbose:
                print(f"{edges[randAB]}, {edges[randCD]}")
        else:
            if verbose:
                print("Skip..")
            i -= 1
        i += 1

    return edges


def dfs(graph, visited, v, component):
    visited[v] = True
    component.append(v)
    for i in range(len(graph)):
        if graph[v][i] == 1 and not visited[i]:
            dfs(graph, visited, i, component)


def longest_subarray(arr):
    max_len = 0
    max_subarr = []
    for subarr in arr:
        if len(subarr) > max_len:
            max_len = len(subarr)
            max_subarr = subarr
    return max_subarr



def all_connected_components(graph):
    n = len(graph)
    visited = [False] * n
    all_components = []
    for i in range(n):
        if not visited[i]:
            component = []
            dfs(graph, visited, i, component)
            all_components.append(component)
    print("Największa składowa grafu: " + str(longest_subarray(all_components)))
    return all_components



# zad 4
def generate_eulerian_graph(num_vertices):
    adjacency_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    even_vertices = list(range(0, num_vertices, 2))

    odd_vertices = list(range(1, num_vertices, 2))

    random.shuffle(odd_vertices)

    for i in range(len(even_vertices)):
        for j in range(i + 1, len(even_vertices)):
            adjacency_matrix[even_vertices[i]][even_vertices[j]] = 1
            adjacency_matrix[even_vertices[j]][even_vertices[i]] = 1

    for i in range(len(odd_vertices)):
        for j in range(i + 1, len(odd_vertices)):
            adjacency_matrix[odd_vertices[i]][odd_vertices[j]] = 1
            adjacency_matrix[odd_vertices[j]][odd_vertices[i]] = 1

    for i in range(len(even_vertices)):
        j = random.randrange(len(odd_vertices))
        adjacency_matrix[even_vertices[i]][odd_vertices[j]] = 1
        adjacency_matrix[odd_vertices[j]][even_vertices[i]] = 1

    return np.array(adjacency_matrix)


def find_eulerian_cycle(adjacency_matrix):
    """
    Finds an Eulerian cycle in the given graph represented by its adjacency matrix.
    Returns a list of vertices in the cycle.
    """
    # Find the starting vertex for the cycle
    start_vertex = 0
    while sum(adjacency_matrix[start_vertex]) == 0:
        start_vertex += 1

    # Initialize the cycle with the starting vertex
    cycle = [start_vertex]

    # Repeat until all edges have been visited
    while True:
        # Find an unused edge from the current vertex
        for next_vertex in range(len(adjacency_matrix)):
            if adjacency_matrix[cycle[-1]][next_vertex] == 1:
                break

        # If all edges have been visited, we're done
        else:
            break

        # Follow the edge to the next vertex
        cycle.append(next_vertex)
        adjacency_matrix[cycle[-2]][next_vertex] = 0
        adjacency_matrix[next_vertex][cycle[-2]] = 0

    return cycle

# zad 5

def generate_k_regular_graph(num_vertices, degree):
    # Sprawdź warunki na stopień grafu
    if degree >= num_vertices or (degree * num_vertices) % 2 != 0:
        print("Nie można stworzyć grafu regularnego o podanych parametrach.")
        return None

    # Stwórz macierz zerową dla macierzy incydencji
    inc_matrix = np.zeros((num_vertices, int(degree * num_vertices / 2)), dtype=int)

    # Generuj graf regularny
    vertex_degrees = np.zeros(num_vertices, dtype=int)  # Licznik stopni wierzchołków

    for col in range(inc_matrix.shape[1]):
        # Szukaj wierzchołka o najmniejszym stopniu
        min_degree_vertex = np.argmin(vertex_degrees)

        # Znajdź pierwszy niepołączony wierzchołek
        connected_vertices = np.where(inc_matrix[:, col] == 1)[0]

        for vertex in range(num_vertices):
            if vertex_degrees[vertex] < degree and vertex not in connected_vertices and vertex != min_degree_vertex:
                # Połącz wierzchołki
                inc_matrix[min_degree_vertex, col] = 1
                inc_matrix[vertex, col] = 1

                # Zwiększ licznik stopnia wierzchołków
                vertex_degrees[min_degree_vertex] += 1
                vertex_degrees[vertex] += 1

                break

    return inc_matrix




#zad6
def is_hamiltonian(graph):
    num_vertices = len(graph)
    visited = [False] * num_vertices

    def dfs(vertex, num_visited):
        visited[vertex] = True
        num_visited += 1
        if num_visited == num_vertices:
            return True
        for neighbor in range(num_vertices):
            if graph[vertex][neighbor] == 1 and not visited[neighbor]:
                if dfs(neighbor, num_visited):
                    return True
        visited[vertex] = False
        return False

    for start_vertex in range(num_vertices):
        if dfs(start_vertex, 0):
            return True

    return False
