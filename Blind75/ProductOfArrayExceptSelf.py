from typing import List

# Using separate prefix and suffix arrays
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        pref = [0] * n
        suff = [0] * n

        pref[0] = suff[n - 1] = 1
        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]
        print(pref)
        for i in range(n - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]
        print(suff)
        for i in range(n):
            res[i] = pref[i] * suff[i] 
        print(res)
        return res

# Prefix and suffix - without using extra arrays - Optimal

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        pref = 1

        # populate with prefix values
        for i in range(0, n):
            res[i] = pref
            pref = nums[i]*pref
        postfix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res