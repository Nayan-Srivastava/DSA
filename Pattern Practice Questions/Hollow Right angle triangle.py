def hollow_triangle(n):
    pattern = []
    for i in range(1, n + 1):
        if i == 1:
            row = '*'
        elif i == n:
            row = '*' * n
        else:
            row = '*' + ' ' * (i - 2) + '*'
        pattern.append(row)
    return pattern


print(hollow_triangle(5))
