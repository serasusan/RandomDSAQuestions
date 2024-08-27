# https://leetcode.com/problems/sort-characters-by-frequency/
from collections import defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:        
        freq = defaultdict(int)
        for ch in s:
            freq[ch]+=1
        
        freq_list = [(count,char) for char,count in freq.items()]
        freq_list.sort(key = lambda x : (-x[0],x[1]))

        result = [ch*f for f,ch in freq_list]
        result_str = ''.join(result)
        return result_str