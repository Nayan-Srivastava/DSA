def diamond_pattern(n):
    pattern = []
    # Upper part (including middle row)
    for i in range(1, n + 1):
        stars = '*' * (2 * i - 1)
        row = stars.center(2 * n - 1)
        pattern.append(row)
    # Lower part (mirror of upper, excluding middle row)
    for i in range(n - 1, 0, -1):
        stars = '*' * (2 * i - 1)
        row = stars.center(2 * n - 1)
        pattern.append(row)
    return pattern

print(diamond_pattern(5))