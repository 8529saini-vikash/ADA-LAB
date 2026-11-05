class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight

    def __repr__(self):
        return f"({self.source}, {self.destination}, {self.weight})"


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, source, destination, weight):
        self.edges.append(Edge(source, destination, weight))

    def _find(self, parent, vertex):
        if parent[vertex] != vertex:
            parent[vertex] = self._find(parent, parent[vertex])
        return parent[vertex]

    def _union(self, parent, rank, first, second):
        root_first = self._find(parent, first)
        root_second = self._find(parent, second)

        if root_first == root_second:
            return False

        if rank[root_first] < rank[root_second]:
            parent[root_first] = root_second
        elif rank[root_first] > rank[root_second]:
            parent[root_second] = root_first
        else:
            parent[root_second] = root_first
            rank[root_first] += 1

        return True

    def kruskal_mst(self):
        parent = list(range(self.vertices))
        rank = [0] * self.vertices
        mst = []

        for edge in sorted(self.edges, key=lambda item: item.weight):
            if self._union(parent, rank, edge.source, edge.destination):
                mst.append(edge)
                if len(mst) == self.vertices - 1:
                    break

        if len(mst) != self.vertices - 1:
            raise ValueError("Graph is disconnected; MST does not exist.")

        return mst

    def prim_mst(self):
        import heapq

        if self.vertices == 0:
            return []

        adjacency = [[] for _ in range(self.vertices)]

        for edge in self.edges:
            adjacency[edge.source].append((edge.weight, edge.destination))
            adjacency[edge.destination].append((edge.weight, edge.source))

        visited = [False] * self.vertices
        visited[0] = True
        heap = []

        for weight, neighbor in adjacency[0]:
            heapq.heappush(heap, (weight, 0, neighbor))

        mst = []

        while heap and len(mst) < self.vertices - 1:
            weight, source, destination = heapq.heappop(heap)

            if visited[destination]:
                continue

            visited[destination] = True
            mst.append(Edge(source, destination, weight))

            for next_weight, neighbor in adjacency[destination]:
                if not visited[neighbor]:
                    heapq.heappush(
                        heap, (next_weight, destination, neighbor)
                    )

        if len(mst) != self.vertices - 1:
            raise ValueError("Graph is disconnected; MST does not exist.")

        return mst


# Creating an edge-weighted graph
graph = Graph(5)

graph.add_edge(0, 1, 2)
graph.add_edge(0, 3, 6)
graph.add_edge(1, 2, 3)
graph.add_edge(1, 3, 8)
graph.add_edge(1, 4, 5)
graph.add_edge(2, 4, 7)
graph.add_edge(3, 4, 9)

print("Kruskal's Minimum Spanning Tree:")
for edge in graph.kruskal_mst():
    print(edge)

print("\nPrim's Minimum Spanning Tree:")
for edge in graph.prim_mst():
    print(edge)
