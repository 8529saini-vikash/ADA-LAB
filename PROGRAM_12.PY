def floyd_warshall(graph):
    n = len(graph)
    distance = [row[:] for row in graph]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distance[i][k] != float("inf") and distance[k][j] != float("inf"):
                    distance[i][j] = min(
                        distance[i][j],
                        distance[i][k] + distance[k][j]
                    )

    return distance


def optimal_bst(keys, freq):
    if len(keys) != len(freq):
        raise ValueError("Keys and frequencies must have equal lengths.")

    n = len(keys)
    if n == 0:
        return 0

    dp = [[0] * n for _ in range(n)]
    prefix = [0] * (n + 1)

    for i in range(n):
        if freq[i] < 0:
            raise ValueError("Frequencies cannot be negative.")
        prefix[i + 1] = prefix[i] + freq[i]
        dp[i][i] = freq[i]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            total_frequency = prefix[j + 1] - prefix[i]
            dp[i][j] = float("inf")

            for root in range(i, j + 1):
                left_cost = dp[i][root - 1] if root > i else 0
                right_cost = dp[root + 1][j] if root < j else 0
                cost = left_cost + right_cost + total_frequency
                dp[i][j] = min(dp[i][j], cost)

    return dp[0][n - 1]


# Floyd-Warshall example (INF represents no direct edge)
INF = float("inf")
graph = [
    [0, 5, INF, 10],
    [INF, 0, 3, INF],
    [INF, INF, 0, 1],
    [INF, INF, INF, 0]
]

print("Floyd-Warshall Shortest Path Matrix:")
for row in floyd_warshall(graph):
    print(row)

# Optimal BST example
keys = [10, 20, 30]
frequencies = [34, 8, 50]

print("\nOptimal Binary Search Tree")
print("Keys:", keys)
print("Frequencies:", frequencies)
print("Minimum Search Cost:", optimal_bst(keys, frequencies))
