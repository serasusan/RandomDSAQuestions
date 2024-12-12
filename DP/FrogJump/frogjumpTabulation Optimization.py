class Solution:
    def frogJump(self, heights):
        n = len(heights)
        prev = 0

        for i in range(1,n):
            oneJump = prev + abs(heights[i] - heights[i-1])

            # Two jumps (only if valid)
            twoJump = float('inf')
            if i > 1:
                twoJump = prev2 + abs(heights[i] - heights[i-2])

            # Take the minimum of oneJump and twoJump
            prev2 = prev
            prev = min(oneJump, twoJump)
        return prev