def sandglass_pattern(n):
    pattern = []
    # Upper part (including middle row)
    for i in range(n):
        stars = '*' * (2 * (n - i) - 1)
        row = stars.center(2 * n - 1)
        pattern.append(row)
    # Lower part (mirror, excluding middle row)
    for i in range(1, n):
        stars = '*' * (2 * i + 1)
        row = stars.center(2 * n - 1)
        pattern.append(row)
    return pattern


print(sandglass_pattern(5))