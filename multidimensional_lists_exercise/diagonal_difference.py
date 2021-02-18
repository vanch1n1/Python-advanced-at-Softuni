n = int(input())
matrix = []
for i in range(n):
    row = [int(el) for el in  input().split(' ')]
    matrix.append(row)
diagonal_sum = 0
oposite_value = 0
row = n - 1
for r in range(len(matrix)):
    oposite_value += matrix[row][r]
    row -= 1
    for c in range(len(matrix)):
        value = matrix[r][c]
        if c == r:
            diagonal_sum += value


print(abs(diagonal_sum - oposite_value))
