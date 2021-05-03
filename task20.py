def transpose(func_matrix):
    for i in range(len(func_matrix) - 1):
        for j in range(i + 1, len(func_matrix[i])):
            func_matrix[i][j], func_matrix[j][i] = func_matrix[j][i], func_matrix[i][j]


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transpose(matrix)
for line in matrix:
    print(*line)
matrix = [[1]]
transpose(matrix)
for line in matrix:
    print(*line)