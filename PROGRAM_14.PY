def solveNQueens(n):
    if n <= 0:
        return []

    solutions = []
    board = [["."] * n for _ in range(n)]
    columns = set()
    diagonal_down = set()
    diagonal_up = set()

    def backtrack(row):
        if row == n:
            solutions.append(["".join(line) for line in board])
            return

        for col in range(n):
            if (
                col in columns
                or row - col in diagonal_down
                or row + col in diagonal_up
            ):
                continue

            board[row][col] = "Q"
            columns.add(col)
            diagonal_down.add(row - col)
            diagonal_up.add(row + col)

            backtrack(row + 1)

            board[row][col] = "."
            columns.remove(col)
            diagonal_down.remove(row - col)
            diagonal_up.remove(row + col)

    backtrack(0)
    return solutions


# Example input
n = 4
solutions = solveNQueens(n)

print("N-Queens Problem")
print("Board Size:", n)
print("Total Solutions:", len(solutions))

for number, solution in enumerate(solutions, 1):
    print("\nSolution", number)
    for row in solution:
        print(row)
