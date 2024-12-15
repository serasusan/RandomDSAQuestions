# Brute force



def triplet(n, arr):
    st = set()

    # check all possible triplets:
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == 0:
                    temp = [arr[i], arr[j], arr[k]]
                    temp.sort()
                    st.add(tuple(temp))

    # store the set elements in the answer:
    ans = [list(item) for item in st]
    return ans

# 2 loops : Hashmap



def triplet(n, arr):
    st = set()

    for i in range(n):
        hashset = set()
        for j in range(i + 1, n):
            # Calculate the 3rd element:
            third = -(arr[i] + arr[j])

            # Find the element in the set:
            if third in hashset:
                temp = [arr[i], arr[j], third]
                temp.sort()
                st.add(tuple(temp))
            hashset.add(arr[j])

    # store the set in the answer:
    ans = list(st)
    return ans




# 2 pointers
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        n = len(nums)
        for i in range(n):
            j = i+1
            k = n-1
            if i>0 and nums[i]==nums[i-1]:
                continue
            while j<k:
                tot_sum = nums[i]+nums[j]+nums[k]
                if tot_sum>0:
                    k-=1
                elif tot_sum<0:
                    j+=1
                else:
                    temp = [nums[i],nums[j],nums[k]]
                    ans.append(temp)
                    j+=1
                    k-=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
        return ans