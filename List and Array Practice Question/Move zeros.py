def move_zeroes(num):
    non_zero = [n for n in num if n != 0]
    zero_count = len(num) - len(non_zero)
    return non_zero + [0] * zero_count

print(move_zeroes([0, 1, 0, 3, 12]))  # Output: [1, 3, 12, 0, 0]
print(move_zeroes([0, 0, 1]))         # Output: [1, 0, 0]