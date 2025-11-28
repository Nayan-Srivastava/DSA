def matrix_reshape(mat, r, c):
    """
    Reshape a 2D matrix into a new matrix with specified rows and columns.

    Parameters:
    mat (List[List[int]]): The original 2D matrix.
    r (int): The number of rows for the reshaped matrix.
    c (int): The number of columns for the reshaped matrix.

    Returns:
    List[List[int]]: The reshaped matrix if possible, otherwise the original matrix.
    """
    original_rows = len(mat)
    original_cols = len(mat[0]) if original_rows > 0 else 0

    # Check if reshape is possible
    if original_rows * original_cols != r * c:
        return mat

    # Flatten the original matrix
    flat_list = [item for row in mat for item in row]

    # Create the reshaped matrix
    reshaped_matrix = []
    for i in range(r):
        new_row = flat_list[i * c:(i + 1) * c]
        reshaped_matrix.append(new_row)

    return reshaped_matrix

mat = [[1, 2], [3, 4]]
r = 1
c = 4
print(matrix_reshape(mat, r, c))  # Output: [[1, 2, 3, 4]]