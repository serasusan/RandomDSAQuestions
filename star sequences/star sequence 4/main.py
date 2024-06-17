n = int(input("Enter the number of rows: "))

for i in range(1,n+1):
    if i==1 or i==n:
        print("*"*i)
    else:
        print("*"+" "*(i-2)+"*")