
n=9

for i in range(n,1,-2):
    if i==1 or i==n:
        print(" "*((n-i)//2) + i*"*")
    else:
        print(" "*((n-i)//2) + "*"+" "*(i-2) + "*")
for i in range(1,n+1,2):
    if i==1 or i==n:
        print(" "*((n-i)//2) + i*"*")
    else:
        print(" "*((n-i)//2) + "*"+" "*(i-2) + "*")

