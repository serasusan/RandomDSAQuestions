# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/1313602005/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashMap = {}
        windowStart = 0
        longestLength = 0
        for windowEnd in range(len(s)):
            char = s[windowEnd]
            if(char in hashMap):
                newWindowStart = hashMap[char]+1
                while(windowStart<newWindowStart):
                    del hashMap[s[windowStart]]
                    windowStart+=1
                windowStart = newWindowStart
            hashMap[char]=windowEnd
            longestLength = max(longestLength,windowEnd-windowStart+1)
            



        return longestLength