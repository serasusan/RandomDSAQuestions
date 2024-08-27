# using backtracking

# def printFirstNNumbers( n):
#     if n<1:
#         return
#     printFirstNNumbers(n-1)
#     print(n)
# printFirstNNumbers(10)


# normal recursion

def printFirstNNumbers(i,n):
    if i>n:
        return
    print(i)
    printFirstNNumbers(i+1,n)

printFirstNNumbers(1,10)