n = int(input("Enter the number of rows: "))

for i in range(1,2*n+1,2):
    if i==1 or i==2*n or i==n: 
        print(" "*(n-(i//2))+"*"*i)

    else:
        print(" "*(n-(i//2))+"*"+" "*(i-2)+"*")
