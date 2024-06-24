n=9
for i in range(1,n,2):
    if i==1:
        print(" "*((n-i)//2) + i*"*")
    else:
        print(" "*((n-i)//2) + "*"+" "*(i-2) + "*")

for i in range(n,0,-2):
    if i==1:
        print(" "*((n-i)//2) + i*"*")
    else:
        print(" "*((n-i)//2) + "*"+" "*(i-2) + "*")