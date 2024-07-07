# An array is given and a given sum k. Find the smallest subarray with sum >= k 
from typing import List 

def smallestSubarray(nums:List[int],k:int) -> int:
    minWindowSize = float('inf')
    currentRunningSum = 0
    windowStart = 0

    for windowEnd in range(len(nums)):
        currentRunningSum += nums[windowEnd]
        if(currentRunningSum>=k):
            minWindowSize = min(minWindowSize,windowEnd-windowEnd+1)
            currentRunningSum-=nums[windowStart]
            windowStart+=1

    return minWindowSize


print(smallestSubarray([4,2,2,7,8,1,2,8,10],8)) 