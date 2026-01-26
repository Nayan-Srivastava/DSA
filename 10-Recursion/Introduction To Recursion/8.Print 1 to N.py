def print1ToN(n):
    if(n<=0): # base Case
        return

    print1ToN(n-1) # Recursion Call - Head

    print(n)

print1ToN(5)



def list1ToN(n):
    """
    1 to N list
    """
    if(n<=0):
        return []

    smallList = list1ToN(n-1)
    smallList.append(n)

    return smallList

print(list1ToN(5))