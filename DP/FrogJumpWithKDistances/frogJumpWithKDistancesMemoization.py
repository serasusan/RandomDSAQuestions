class Solution:
    def frogJump(self, heights,k):
        n = len(heights)
        dp = [-1]*(n)
        return self.func(n-1,heights,dp,k)

    def func(self,ind, heights,dp,k):
        if ind == 0:
            return 0
        if dp[ind]!=-1:
            return dp[ind]
        val = float('inf')
        for j in range(1,k+1):
            if ind - j >= 0:
                jump = self.func(ind-j,heights,dp,k)+abs(heights[ind]-heights[ind-j])
                val = min(jump,val)
        dp[ind] = val
        return dp[ind]