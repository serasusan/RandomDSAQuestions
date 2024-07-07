from typing import List

def findMaxAverage( nums: List[int], k: int) -> float:
        max_value = float('-inf')
        currentRunningSum = 0
        for i in range(len(nums)):
            currentRunningSum += nums[i]
            if(i>=k-1):
                max_value = max(currentRunningSum,max_value)
                currentRunningSum -= nums[i-(k-1)]
        return max_value/k

print(findMaxAverage([1,12,-5,-6,50,3],4))