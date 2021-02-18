rows, columns = [ int(el) for el in input().split()]
word = input()
matrix = []
for row in range(rows):
    matrix.append([0 for el in range(columns)])
index_word = 0
for row in range(rows):
    for column in range(columns):
        matrix[row][column] = word[index_word]
        index_word += 1
        if index_word == len(word):
            index_word = 0
for row in range(len(matrix)):
    if row % 2 == 1:
        matrix[row].reverse()
    print(''.join(matrix[row]))
