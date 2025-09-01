def numbered_pyramid(n):
    pattern = []
    for i in range(1, n + 1):
        numbers = ' '.join(str(j) for j in range(1, i + 1))
        spaces = ' ' * (n - i)
        row = spaces + numbers + spaces
        pattern.append(row)
    return pattern

print(numbered_pyramid(5))