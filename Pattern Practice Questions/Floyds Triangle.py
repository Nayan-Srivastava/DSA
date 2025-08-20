def floyds_triangle(n):
    result = []
    num = 1
    for i in range(1, n + 1):
        row = []
        for _ in range(i):
            row.append(str(num))
            num += 1
        result.append(' '.join(row))
    return result

print(floyds_triangle(5))