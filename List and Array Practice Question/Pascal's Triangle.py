def generate(numRows):
    if numRows == 0:
        return []

    triangle = [[1]]  # First row

    for row in range(1, numRows):
        new_row = [1]  # Start with 1
        for j in range(1, row):
            new_row.append(triangle[row-1][j-1] + triangle[row-1][j])
        new_row.append(1)  # End with 1
        triangle.append(new_row)

    return triangle

numRows = 3
print(generate(numRows))
