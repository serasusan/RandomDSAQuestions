class Solution:
    def climbStairs(self, n):
        if n == 0:
            return 1
        if n == 1:
            return 1
        
        dp = [0] * (n + 1)  # Create a dp array of size (n+1)
        
        # Base cases
        dp[0] = 1
        dp[1] = 1
        
        # Fill the dp table iteratively
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]  # Transition formula
        
        return dp[n]  # Return the result for n

