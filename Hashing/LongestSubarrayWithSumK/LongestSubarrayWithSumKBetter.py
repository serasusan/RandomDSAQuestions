# This is the optimal solution for arrays with +ve,-ve & 0.
# But only a better solution for arrays with +ve & 0.
# There is another optimal solution using 2 pointers

class Solution:
    def longestSubarray(self, nums, k):
        n = len(nums)

        preSumMap = {}
        maxLen = 0
        curr_sum=0

        for i in range(n):
            curr_sum += nums[i]

            if curr_sum==k:
                maxLen = max(maxLen,i+1)
            else:
                rem = curr_sum-k
                if rem in preSumMap:
                    length = i-preSumMap[rem]
                    maxLen = max(maxLen, length)

            if curr_sum not in preSumMap:
                preSumMap[curr_sum]=i

        return maxLen