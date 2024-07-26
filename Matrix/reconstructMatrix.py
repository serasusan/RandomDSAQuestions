# https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/submissions/1334357152/

from typing import List


class Solution:
    def reconstructMatrix( upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        n = len(colsum)

        if upper+lower!=sum(colsum):
            return []
        
        a = [[0 for i in range(n)] for j in range(2)]
        
        for j in range(n):
            if colsum[j]==2:
                if upper>0 and lower>0:
                    a[0][j]=1
                    a[1][j]=1
                    upper-=1
                    lower-=1
                else:
                    return []
            elif colsum[j]==1:
                if upper>lower: 
                    a[0][j]=1
                    a[1][j]=0
                    upper-=1
                elif lower>=upper:
                    a[0][j]=0
                    a[1][j]=1 
                    lower-=1
        if upper == 0 and lower == 0:
                return a
        else:
                return []


upper = 2
lower = 1
colsum = [1,1,1]
print(Solution.reconstructMatrix(upper,lower,colsum))