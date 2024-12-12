class Solution:
    def frogJump(self, heights):
        n = len(heights)
        dp = [-1]*(n)
        dp[0] = 0
        for i in range(1,n):
            oneJump = dp[i-1] + abs(heights[i] - heights[i-1])

            # Two jumps (only if valid)
            twoJump = float('inf')
            if i > 1:
                twoJump = dp[i-2] + abs(heights[i] - heights[i-2])

            # Take the minimum of oneJump and twoJump
            dp[i] = min(oneJump, twoJump)
        return dp[n-1]