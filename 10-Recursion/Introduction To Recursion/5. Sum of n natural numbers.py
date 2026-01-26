import sys
sys.setrecursionlimit(5000) #Increasing recursion limit to avoid RecursionError for large n

def sumOfNumbersTillN(n):
    if(n==1):
        return 1 #Base Case (1)

    ans = n + sumOfNumbersTillN(n-1)

    return ans


#Testing the function
print(sumOfNumbersTillN(5))
print(sumOfNumbersTillN(1000))
