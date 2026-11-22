class TSPSolver:
    def solve_tsp(self, dist_matrix):
        n = len(dist_matrix)

        if n == 0:
            return 0
        if any(len(row) != n for row in dist_matrix):
            raise ValueError("Distance matrix must be square.")
        if n == 1:
            return 0

        full_mask = (1 << n) - 1
        memo = {}

        def tsp(mask, current):
            if mask == full_mask:
                return dist_matrix[current][0]

            state = (mask, current)
            if state in memo:
                return memo[state]

            best_cost = float("inf")

            for city in range(n):
                if not (mask & (1 << city)):
                    next_mask = mask | (1 << city)
                    cost = (
                        dist_matrix[current][city]
                        + tsp(next_mask, city)
                    )
                    best_cost = min(best_cost, cost)

            memo[state] = best_cost
            return best_cost

        return tsp(1, 0)


# Example distance matrix
dist_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

solver = TSPSolver()
print("Travelling Salesperson Problem")
print("Minimum Tour Cost:", solver.solve_tsp(dist_matrix))
