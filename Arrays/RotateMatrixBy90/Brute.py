class Solution:
    def rotateMatrix(self, matrix):
        n = len(matrix[0])
        rotated = [[0]*n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                rotated[j][n-i-1]=matrix[i][j]
        
        for i in range(n):
            matrix[i]=rotated[i]
        return rotated