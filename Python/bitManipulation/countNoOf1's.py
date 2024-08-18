n = 5
c = 0
while(n>1):
    if(n%2==1):
        c+=1
    n = n//2

if n==1: c+=1
print("Count is {}".format(c))

n = 5
c = 0

while(n>1):
    c+= n&1
    n = n>>1
if n==1: c+=1
print("Count is {}".format(c))

# another approach
n = 5
c = 0
while(n!=0):
    n = n & n-1 #each time the rightmost set bit is deleted
    c += 1

print("Count is {}".format(c))
