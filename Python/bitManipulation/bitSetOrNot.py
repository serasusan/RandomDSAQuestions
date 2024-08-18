a = 13
i = 2

# using left shift operator 
if (a & (1<<i)): 
    print("set")
else:
    print("not set")

# using right shift operator
if((a>>i) & 1):
    print("set")
else:
    print("not set")