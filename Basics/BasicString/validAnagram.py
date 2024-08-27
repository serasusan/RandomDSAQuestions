from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t)!=len(s):
            return False
        hashMap = defaultdict(int)
        for i in range(len(s)):
            hashMap[s[i]]+=1
        for j in range(len(t)):
            if( hashMap[t[j]]==0 or t[j] not in hashMap.keys()):
                return False
            hashMap[t[j]]-=1
            print(hashMap)
        return True
    
s=Solution()
print(s.isAnagram("aabbbb","aaaabb"))