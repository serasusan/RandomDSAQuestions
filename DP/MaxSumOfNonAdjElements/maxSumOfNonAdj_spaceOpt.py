class Solution:
    def nonAdjacent(self, nums):
        n = len(nums)
        dp = [-1]*(n+1)

        prev=nums[0]
        prev2 = 0

        for i in range(1,n):
            pick = nums[i];
            if i>1:
                pick = pick+prev2
            notpick = 0 + prev

            
            curr = max(pick,notpick)
            prev2 = prev
            prev = curr
        return prev

                        
                        