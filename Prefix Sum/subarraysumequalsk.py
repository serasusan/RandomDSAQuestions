class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            sumarr = 0
            for j in range(i,len(nums)):
                sumarr += nums[j]
                if sumarr == k:
                    count +=1


        return count


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currsum = 0
        hashmap = {0:1}
        cnt = 0
        for num in nums:
            currsum += num
            if currsum-k in hashmap:
                cnt += hashmap[currsum-k]
            
            hashmap[currsum] = hashmap.get(currsum,0)+1
        return cnt


