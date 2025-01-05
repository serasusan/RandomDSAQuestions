class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)-1
        w = n
        l = 0
        r = n
        maxArea = float(-inf)
        while r>l:
            area = w*(min(height[l],height[r]))
            maxArea = max(area,maxArea)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
            w = w-1
        return maxArea