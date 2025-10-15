def search_matrix(matrix, target):
    m,n = len(matrix), len(matrix[0])
    for row in matrix:
        if row[0] <= target <= row[-1]:
            left, right = 0, n - 1
            while left <= right:
                mid = left + (right - left) // 2
                if row[mid] == target:
                    return True
                elif row[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return False

matrix = [[1, 3, 5, 7],
                 [10, 11, 16, 20],
                 [23, 30, 34, 60]]
target = 13
print(search_matrix(matrix, target))  # Output: False