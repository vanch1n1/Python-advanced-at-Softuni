rows, columns = [int(el) for el in input().split(' ')]
matrix = []
for row in range(rows):
    row = input().split(' ')
    matrix.append(row)
line = input()
while line != 'END':
    command = line.split(' ')
    try:
        coordinates = [int(el) for el in command[1:]]
    except:
        print('Invalid input!')
    if command[0] != 'swap':
        print('Invalid input!')
    elif len(coordinates) != 4:
        print('Invalid input!')
    elif coordinates[0] > rows or coordinates[1] > columns or coordinates[2] > rows or coordinates[3] > columns:
        print('Invalid input!')
    else:
        current_row = int(coordinates[0])
        current_col = int(coordinates[1])
        row_to_swap = int(coordinates[2])
        col_to_swap = int(coordinates[3])
        index_to_replace = matrix[current_row][current_col]
        matrix[current_row][current_col] = matrix[row_to_swap][col_to_swap]
        matrix[row_to_swap][col_to_swap] = index_to_replace
        for row in matrix:
            print(f"{' '.join(row)}")
    line = input()

