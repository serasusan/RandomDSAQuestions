# Given the row number r and the column number c, find out the element at position (r , c).

# n -> row
# r -> column

def nCr(n,r):
    if r>n:
        print("Invalid column")
        return 
    
    if r>n-r:
        r = n-r

    res = 1

    for i in range(r):
        res = res*(n-i)
        res = res//(i+1)
    return res

# to find 3rd row and 3th column
print(nCr(2,2))