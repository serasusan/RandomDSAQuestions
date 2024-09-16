# For Arrays with +ve and 0 elements
# Using 2 pointers

class Solution:
    def longestSubarray(self, nums, k):
        n = len(nums)
        left = 0
        right = 0
        curr_sum = nums[0]
        maxlen = 0

        while right<n:
            
            while curr_sum>k and left<=right:
                curr_sum-=nums[left]
                left+=1
            if curr_sum==k:
                maxlen = max(maxlen,right-left+1)
            right+=1
            if right<n:
                curr_sum+=nums[right]

        return maxlen