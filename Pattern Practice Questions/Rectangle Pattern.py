def rectanle(n,m):
    """
    Function to create a rectangle pattern of '*' characters.
    :param n: Number of rows in the rectangle
    :param m: Number of columns in the rectangle
    :return: List of strings representing the rectangle pattern
    """
    return ['*'*m for i in range(n)]

n,m = map(int, input("Enter two numbers: ").split())
print(rectanle(n,m))