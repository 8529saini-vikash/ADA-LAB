def knapsack_01(weights, values, capacity):
    n = len(weights)

    if len(weights) != len(values):
        raise ValueError("Weights and values must have the same length.")
    if capacity < 0 or any(weight < 0 for weight in weights):
        raise ValueError("Weights and capacity cannot be negative.")

    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for current_capacity in range(capacity + 1):
            dp[i][current_capacity] = dp[i - 1][current_capacity]

            if weights[i - 1] <= current_capacity:
                include_value = (
                    values[i - 1]
                    + dp[i - 1][current_capacity - weights[i - 1]]
                )
                dp[i][current_capacity] = max(
                    dp[i][current_capacity], include_value
                )

    return dp[n][capacity]


# Example input
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

print("0/1 Knapsack using Dynamic Programming")
print("Weights:", weights)
print("Values:", values)
print("Capacity:", capacity)
print("Maximum Value:", knapsack_01(weights, values, capacity))
