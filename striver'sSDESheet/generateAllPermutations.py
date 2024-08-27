from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        ans = []
        def generateAllPermut(index, arr):
            n = len(arr)
            if index == n:
                ans.append(arr[:])  # Append a copy of arr, not the reference
                return
            for i in range(index, n):
                arr[index], arr[i] = arr[i], arr[index]  # Swap
                generateAllPermut(index + 1, arr)  # Recur for the next index
                arr[index], arr[i] = arr[i], arr[index]  # Swap back to backtrack

            return ans

        generateAllPermut(0,nums)
        print(ans)
        for i in range(len(ans)):
            if ans[i]==nums:
                return ans[i+1]

s = Solution()
nums = [1,2,3]
print(s.nextPermutation(nums))