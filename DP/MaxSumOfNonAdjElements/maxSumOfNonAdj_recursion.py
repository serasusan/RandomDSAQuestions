class Solution:
    def nonAdjacent(self, nums):
        n = len(nums)
        return self.func(n-1,nums)

    def func(self,ind,nums):
        if ind == 0:
            return nums[ind]
        if ind < 0:
            return 0
        
        pick = nums[ind]+self.func(ind-2,nums)
        notpick = 0 + self.func(ind-1,nums)
        return max(pick,notpick)
