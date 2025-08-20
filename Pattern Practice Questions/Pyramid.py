def pyramid(n):
    pattern = []
    for i in range(n):
        spaces = ' ' * (n - i - 1)
        stars = '*' * (2 * i + 1)
        pattern.append(spaces + stars + spaces)
    return pattern

print(pyramid(5))