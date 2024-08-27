from collections import defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:        
        freq = defaultdict(int)
        for ch in s:
            freq[ch]+=1
        
        freq.sort(key= lambda x:freq[1])

        print(freq) 