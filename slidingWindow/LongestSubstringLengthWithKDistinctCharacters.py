# Longest substring length with k distinct characters

from typing import List

def longestSubstring(s:List[int],k:int):
    hashMap = {}
    windowStart = 0
    longestLength = 0
    for windowEnd in range(len(s)):
        # if(s[windowEnd] in hashMap):
        #     hashMap[s[windowEnd]]+=1
        # else:
        #     hashMap[s[windowEnd]]=1

        hashMap[s[windowEnd]] = hashMap.get(s[windowEnd],0) + 1

        while(len(hashMap)>k):
            hashMap[s[windowStart]]-=1
            if(hashMap[s[windowStart]]==0):
                del hashMap[s[windowStart]]            
            windowStart+=1

        longestLength = max(longestLength,windowEnd-windowStart+1)
        
    return longestLength

print(longestSubstring("eceba",2))




            
        