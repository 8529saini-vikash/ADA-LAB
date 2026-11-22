class GraphBacktracker:
    def __init__(self, graph):
        self.graph = graph
        self.vertices = len(graph)

    def graph_coloring(self, m):
        colors = [0] * self.vertices

        def is_safe(vertex, color):
            for neighbor in range(self.vertices):
                if self.graph[vertex][neighbor] and colors[neighbor] == color:
                    return False
            return True

        def solve(vertex):
            if vertex == self.vertices:
                return True

            for color in range(1, m + 1):
                if is_safe(vertex, color):
                    colors[vertex] = color

                    if solve(vertex + 1):
                        return True

                    colors[vertex] = 0

            return False

        return colors[:] if solve(0) else []

    def hamiltonian_cycle(self):
        if self.vertices == 0:
            return []

        path = [0]

        def solve():
            if len(path) == self.vertices:
                return self.graph[path[-1]][path[0]] == 1

            for vertex in range(1, self.vertices):
                if vertex not in path and self.graph[path[-1]][vertex] == 1:
                    path.append(vertex)

                    if solve():
                        return True

                    path.pop()

            return False

        if solve():
            return path + [path[0]]
        return []


# Example adjacency matrix
graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]

solver = GraphBacktracker(graph)

print("Graph Coloring")
coloring = solver.graph_coloring(3)
print("Vertex Colors:", coloring if coloring else "No valid coloring exists.")

print("\nHamiltonian Cycle")
cycle = solver.hamiltonian_cycle()
print("Hamiltonian Cycle:", cycle if cycle else "No Hamiltonian Cycle exists.")
