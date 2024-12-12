# Approach 1
from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            sorted_str = tuple(sorted(s))
            print(sorted_str)
            res[sorted_str].append(s)
        return list(res.values())
sol = Solution()
print(sol.groupAnagrams(["act","pots","tops","cat","stop","hat"]))

# Approach 2

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())