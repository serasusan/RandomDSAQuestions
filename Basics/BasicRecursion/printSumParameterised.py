def printSum(i,s):
    if i==0:
        return s
    return printSum(i-1,s+i)

print(printSum(5,0))