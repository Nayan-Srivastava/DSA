def hollow(n):
    if n == 1:
        return ['*']
    if n == 2:
        return ['**', '**']
    top_bottom = '*' * n
    middle = '*' + ' ' * (n - 2) + '*'
    return [top_bottom] + [middle] * (n - 2) + [top_bottom]

print(hollow(int(input("Enter a number: "))))