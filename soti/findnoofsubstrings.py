# Q U E S T I O N
# Given a string A of length n and B of length m
# Find the number of substring of A present in B or no of substrings of A that B is made of
# not sure if the answer is correct

A = "cab"
n = len(A)
B = "abcabc"
m = len(B)


end = 0
c = 0
substring = []
for i in range(n):
    for j in range(i+1,n+1):
        substring.append(A[i:j])
print(substring)
while end < m:
    s = B[end]
    while s in substring and end<m:
        print(s,s in substring)
        end+=1
        if end<m:
            s+=B[end]
    c+=1
print(c)
