class Solution:
    def climbStairs(self, n):
        
        # Base cases
        prev2 = 1
        prev = 1
        
        for i in range(2, n + 1):
            curr = prev2 + prev  # Transition formula
        
        return curr  # Return the result for n

