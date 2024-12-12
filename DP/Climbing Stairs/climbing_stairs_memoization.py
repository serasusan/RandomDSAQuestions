class Solution:
    def climbStairs(self, n):
        dp = [-1]*(n+1)
        return self.func(n,dp)
    
    def func(self,n,dp):
        # here each step is an index
        if n == 0:
            return 1
        if n == 1:
            return 1
        
        if dp[n]!=-1:
            return dp[n]
        # Taking one step at a time
        oneStep = self.func(n-1,dp)

        # Taking two steps at a time
        twoSteps = self.func(n-2,dp)
        dp[n] = oneStep + twoSteps
        return dp[n]
