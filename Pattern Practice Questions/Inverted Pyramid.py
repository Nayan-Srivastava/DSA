def pyramid(n):
    pattern = []
    for i in range(n, 0, -1):
        spaces = ' ' * (n - i)
        stars = '*' * (2 * i - 1)
        pattern.append(spaces + stars + spaces)
    return pattern

print(pyramid(5))