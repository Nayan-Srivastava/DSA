def triangle(n):
    return [(' '*(n-i) +'*'*i) for i in range(1, n+1)]
print(triangle(5))
