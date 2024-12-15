from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        store = set(nums)

        for num in nums:
            streak, curr = 0, num
            while curr in store:
                streak += 1
                curr += 1
            res = max(res, streak)
        return res

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0

        if not nums:
            return 0
        nums = sorted(nums)
        print(nums)
        n = len(nums)
        i = 0
        curr = nums[0]
        streak = 0
        while i<n:
            if curr!=nums[i]:
                streak = 0
                curr = nums[i]
            while i<n and curr==nums[i]:
                i+=1
            curr+=1
            streak+=1
            print(curr,streak)
            res = max(res,streak)

        return res


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        hashset = set(nums)

        for num in nums:
            if num-1 not in hashset: # Indicates this is the starting
                length = 1
                while num+length in hashset:
                    length += 1
                res = max(res,length)
        return res
        
        n = len(nums)
        i = 0
        curr = nums[0]
        streak = 0
        while i<n:
            if curr!=nums[i]:
                streak = 0
                curr = nums[i]
            while i<n and curr==nums[i]:
                i+=1
            curr+=1
            streak+=1
            print(curr,streak)
            res = max(res,streak)

        return res
