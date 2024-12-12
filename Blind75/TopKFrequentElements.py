class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        
        for num in nums:
            count[num] = 1 + count.get(num,0)
        
        #sort using value - using sorted
        sorted_arr = sorted(count.items(),key = lambda x:x[1],reverse=True)

        res = [item[0] for item in sorted_arr[:k]]
        return res
        
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num,0)
        
        heap = []
        # Push (-freq,num in heap)
        for num,freq in count.items():
            heapq.heappush(heap,(-freq,num))
        result = []

        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        return result
    
# Bucket Sort
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = 1 + count.get(n,0)
        for n,c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res