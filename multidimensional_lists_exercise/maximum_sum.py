rows, columns = [int(el) for el in input().split(' ')]
matrix = []
for row in range(rows):
    row = [int(el) for el in input().split(' ')]
    matrix.append(row)

current_sum = 0
best_sum = -99999999
for r in range(len(matrix) - 2):
    for c in range(columns- 2):
        current_sum += matrix[r][c]
        current_sum += matrix[r][c + 1]
        current_sum += matrix[r + 1][c]
        current_sum += matrix[r + 1][c + 1]
        current_sum += matrix[r + 2][c + 0]
        current_sum += matrix[r + 0][c + 2]
        current_sum += matrix[r + 2][c + 2]
        current_sum += matrix[r + 1][c + 2]
        current_sum += matrix[r + 2][c + 1]
        if current_sum > best_sum:
            best_sum = current_sum
            row_index = r
            column_index = c
        current_sum = 0
print(f'Sum = {best_sum}')
sub_matrix = [[],[],[]]
for r in range((len(matrix))):
    for c in range(columns):
        if r == row_index and c == column_index:
            sub_matrix[0].append(str(matrix[r][c]))
            sub_matrix[0].append(str(matrix[r][c + 1]))
            sub_matrix[0].append(str(matrix[r + 0][c + 2]))
            sub_matrix[1].append(str(matrix[r + 1][c]))
            sub_matrix[1].append(str(matrix[r + 1][c + 1]))
            sub_matrix[1].append(str(matrix[r + 1][c + 2]))
            sub_matrix[2].append(str(matrix[r + 2][c + 0]))
            sub_matrix[2].append(str(matrix[r + 2][c + 1]))
            sub_matrix[2].append(str(matrix[r + 2][c + 2]))
for row in sub_matrix:
    print(f"{' '.join(row)}")
