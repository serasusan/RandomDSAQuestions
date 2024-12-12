class Solution:
    def frogJump(self, heights):
        n = len(heights)
        dp = [-1]*(n)
        return self.func(n-1,heights,dp)

    def func(self,ind, heights,dp):
        if ind == 0:
            return 0
        if dp[ind]!=-1:
            return dp[ind]
        twoJump = float('inf')
        oneJump = self.func(ind-1,heights,dp) + abs(heights[ind-1]-heights[ind])
        if ind>1:
            twoJump = self.func(ind-2,heights,dp) + abs(heights[ind-2]-heights[ind])
        dp[ind]= min(oneJump,twoJump)
        return dp[ind]