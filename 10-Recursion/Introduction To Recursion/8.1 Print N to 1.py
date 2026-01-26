def printNto1(n):
    if(n<=0): # base Case
        return

    print(n)
    printNto1(n-1) # Recursion - Tail Recursion


printNto1(5)

def listNto1(n):
    if(n<=0): # base Case
        return []

    lst = listNto1(n-1) # Recursion
    lst.insert(0, n) # Processing
    return lst

print(listNto1(5))