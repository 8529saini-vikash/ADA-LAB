class ShortestPath:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, source, destination, weight):
        self.edges.append((source, destination, weight))

    def dijkstra(self, src):
        import heapq

        if not 0 <= src < self.vertices:
            raise ValueError("Source vertex is out of range.")

        if any(weight < 0 for _, _, weight in self.edges):
            raise ValueError("Dijkstra's algorithm requires non-negative weights.")

        adjacency = [[] for _ in range(self.vertices)]

        for u, v, weight in self.edges:
            adjacency[u].append((v, weight))

        distances = [float("inf")] * self.vertices
        distances[src] = 0
        priority_queue = [(0, src)]

        while priority_queue:
            current_distance, vertex = heapq.heappop(priority_queue)

            if current_distance != distances[vertex]:
                continue

            for neighbor, weight in adjacency[vertex]:
                new_distance = current_distance + weight

                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(
                        priority_queue, (new_distance, neighbor)
                    )

        return distances

    def bellman_ford(self, src):
        if not 0 <= src < self.vertices:
            raise ValueError("Source vertex is out of range.")

        distances = [float("inf")] * self.vertices
        distances[src] = 0

        for _ in range(self.vertices - 1):
            updated = False

            for u, v, weight in self.edges:
                if distances[u] != float("inf"):
                    new_distance = distances[u] + weight

                    if new_distance < distances[v]:
                        distances[v] = new_distance
                        updated = True

            if not updated:
                break

        for u, v, weight in self.edges:
            if (
                distances[u] != float("inf")
                and distances[u] + weight < distances[v]
            ):
                return "Error: Negative weight cycle detected."

        return distances


# Creating a weighted directed graph
graph = ShortestPath(5)

graph.add_edge(0, 1, 10)
graph.add_edge(0, 2, 5)
graph.add_edge(1, 2, 2)
graph.add_edge(1, 3, 1)
graph.add_edge(2, 1, 3)
graph.add_edge(2, 3, 9)
graph.add_edge(2, 4, 2)
graph.add_edge(4, 3, 6)

print("Dijkstra's Shortest Distances:")
print(graph.dijkstra(0))

print("\nBellman-Ford Shortest Distances:")
print(graph.bellman_ford(0))
