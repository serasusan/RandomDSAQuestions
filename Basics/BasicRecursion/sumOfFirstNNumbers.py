class Solution:
    def NnumbersSum(self, N):
        if N == 1: return 1
        return self.NnumbersSum(N-1)+N
    
s = Solution()
print(s.NnumbersSum(10))