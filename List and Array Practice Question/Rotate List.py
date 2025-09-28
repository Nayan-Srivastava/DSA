def rotate_left(ARR, D):
    return ARR[D:] + ARR[:D]

# Example usage:
print(rotate_left([1, 2, 3, 4, 5], 2))  # Output: [3, 4, 5, 1, 2]