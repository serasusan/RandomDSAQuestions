from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        prefixSum = [0] * n
        prefixSum[0] = nums[0]
        
        # Calculate prefix sums
        for i in range(1, n):
            prefixSum[i] = prefixSum[i-1] + nums[i]
        print("prefixSum:", prefixSum)

        # Initialize variables
        maxVal = prefixSum[0]
        minPrefix = 0  # This tracks the minimum prefix sum seen so far
        
        # Iterate through prefix sums to find the maximum subarray sum
        for i in range(n):
            # Calculate potential max subarray sum by subtracting minPrefix
            maxVal = max(maxVal, prefixSum[i] - minPrefix)
            
            # Update minPrefix to the current prefixSum[i] for future subarrays
            minPrefix = min(minPrefix, prefixSum[i])

        return maxVal
