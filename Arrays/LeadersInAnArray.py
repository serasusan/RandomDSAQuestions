# Leaders in an Array

# Given an integer array nums, return a list of all the leaders in the array.

# A leader in an array is an element whose value is strictly greater than all elements to its right in the given array. 
# The rightmost element is always a leader. The elements in the leader array must appear in the order they appear in the nums array.

class Solution:
    def leaders(self, nums):
        l = []
        res = []
        for i in range(len(nums)-1):
            l.append(max(nums[i+1:]))
        for i in range(len(nums)-1):
            if nums[i]>l[i]:
                res.append(nums[i])
        res.append(nums[len(nums)-1])
        return res
    
# O(n^2)