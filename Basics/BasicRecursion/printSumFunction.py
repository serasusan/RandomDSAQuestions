def printSum(i):
    if i==0:
        return 0
    return i+printSum(i-1)

print(printSum(5))