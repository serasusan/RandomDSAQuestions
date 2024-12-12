class Solution:
    def frogJump(self, heights,k):
        n = len(heights)
        dp = [-1]*(n)
        dp[0] = 0
        for i in range(1 ,n):
            minStep = float('inf')
            for j in range(1,k+1):
                if i-j>=0:
                    Jump = dp[i-j] + abs(heights[i] - heights[i-j])
                minStep = min(minStep,Jump)
            dp[i]=minStep
        return dp[n-1]