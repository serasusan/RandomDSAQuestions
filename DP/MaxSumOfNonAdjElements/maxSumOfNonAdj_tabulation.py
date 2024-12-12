class Solution:
    def nonAdjacent(self, nums):
        n = len(nums)
        dp = [-1]*(n+1)

        dp[0]=nums[0]

        for i in range(1,n):
            pick = nums[i];
            if i>1:
                pick = pick+dp[i-2]
            notpick = 0 + dp[i-1]

            dp[i] = max(pick,notpick)
        return dp[n-1]

                        