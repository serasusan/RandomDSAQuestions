# def printReverse(i):
#     if i<1:
#         return 
#     print(i)
#     printReverse(i-1)

# printReverse(10)

# backtracking
def printReverse(i,n):
    if i>n:
        return

    printReverse(i+1,n)
    print(i)

printReverse(1,10)