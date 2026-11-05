
def fractional_knapsack(weights, values, capacity):
    items = sorted(
        zip(weights, values),
        key=lambda item: item[1] / item[0],
        reverse=True
    )

    total_profit = 0.0

    for weight, value in items:
        if capacity <= 0:
            break

        if weight <= capacity:
            total_profit += value
            capacity -= weight
        else:
            total_profit += (value / weight) * capacity
            capacity = 0

    return total_profit


def job_scheduling(jobs):
    # Each job is represented as (job_id, deadline, profit)
    jobs = sorted(jobs, key=lambda job: job[2], reverse=True)

    max_deadline = max(job[1] for job in jobs)
    slots = [None] * max_deadline
    total_profit = 0

    for job_id, deadline, profit in jobs:
        for slot in range(min(deadline, max_deadline) - 1, -1, -1):
            if slots[slot] is None:
                slots[slot] = job_id
                total_profit += profit
                break

    sequence = [job for job in slots if job is not None]

    return total_profit, sequence


# Fractional Knapsack Example
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50

print("Fractional Knapsack")
print("Maximum Profit:", fractional_knapsack(weights, values, capacity))


# Job Scheduling Example
jobs = [
    ("J1", 2, 100),
    ("J2", 1, 19),
    ("J3", 2, 27),
    ("J4", 1, 25),
    ("J5", 3, 15)
]

profit, sequence = job_scheduling(jobs)

print("\nJob Scheduling")
print("Optimal Job Sequence:", sequence)
print("Maximum Profit:", profit)