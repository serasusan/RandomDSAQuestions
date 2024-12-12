class Solution:
    def nonAdjacent(self, nums):
        n = len(nums)
        dp = [-1]*(n+1)
        return self.func(n-1,nums,dp)

    def func(self,ind,nums,dp):
        if ind == 0:
            return nums[ind]
        if ind < 0:
            return 0
        if dp[ind]!=-1:
            return dp[ind]
                        
        pick = nums[ind]+self.func(ind-2,nums,dp)
        notpick = 0 + self.func(ind-1,nums,dp)
        dp[ind] = max(pick,notpick)
        return dp[ind]
