rows, columns = [int(el) for el in input().split(' ')]
matrix = []

for r in range(rows):
    row = input().split(' ')
    matrix.append(row)
counter = 0
for r in range(rows - 1):
    for c in range(columns - 1):
        current_element = matrix[r][c]
        next_element_same_row = matrix[r][c+1]
        element_next_row =  matrix[r+1][c]
        element_next_row_next_column = matrix[r + 1][c + 1]
        if current_element == next_element_same_row  and next_element_same_row == element_next_row and element_next_row == element_next_row_next_column:
            match = True
            counter +=1


print(counter)