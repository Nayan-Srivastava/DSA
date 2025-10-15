def rotate_90(matrix):
    return [list(reversed(col)) for col in zip(*matrix)]

def can_be_rotated(mat, target):
    mat = rotate_90(mat)

    for _ in range(4):
        if mat == target:
            return True
        mat = rotate_90(mat)

    return False

mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
target = [[1, 1, 1], [0, 1, 0], [0, 3, 0]]

print(can_be_rotated(mat, target))  # Output: True