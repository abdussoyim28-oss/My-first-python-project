def add_matrices_nested_loops(matrix1, matrix2):
    """
    Adds two matrices using nested loops.
    Assumes both matrices have the same dimensions.
    """
    rows = len(matrix1)
    cols = len(matrix1[0])
    
    result_matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            result_matrix[i][j] = matrix1[i][j] + matrix2[i][j]
    return result_matrix

# Example usage:
matrix_A = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

matrix_B = [[9, 8, 7],
            [6, 5, 4],
            [3, 2, 1]]

sum_matrix_nested = add_matrices_nested_loops(matrix_A, matrix_B)
print("Matrix sum (nested loops):")
for row in sum_matrix_nested:
    print(row)
