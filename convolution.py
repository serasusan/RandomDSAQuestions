# Matrix Transpose

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


for i in range(len(A)):
    for j in range(i,len(A[0])):
        A[i][j], A[j][i] = A[j][i], A[i][j]

# now multiply the matrix B with A transpose

print(A)