from collections import defaultdict


class Solution:
    def isomorphicString(self, s, t):
        #your code goes here
        if len(s)!=len(t):
            return False

        hashMap = defaultdict(int)
        for i in range(len(s)):
            if s[i] in hashMap:
                if hashMap[s[i]]!=t[i]:
                    return False
            else:
                if t[i] in hashMap.values():
                    return False
                hashMap[s[i]]=t[i]
        return True