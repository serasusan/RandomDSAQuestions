from collections import defaultdict

class Solution:
    def secondMostFrequentElement(self, nums):
        # Create a frequency hashmap
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1
        
        # Debug: print frequency hashmap
        print(f"Frequency Map: {hashmap}")

        # Get all unique frequencies and sort them in descending order
        frequencies = sorted(set(hashmap.values()), reverse=True)

        # Debug: print sorted frequencies
        print(f"Frequencies: {frequencies}")

        # Check if there is a second highest frequency
        if len(frequencies) < 2:
            return None  # No second most frequent element

        secondFreq = frequencies[1]

        # Find the smallest element with the second highest frequency
        reqVal = min(key for key, value in hashmap.items() if value == secondFreq)
        
        return reqVal

# Example usage
s = Solution()
nums = [1, 2, 2, 3, 3, 3]
print(s.secondMostFrequentElement(nums))  # Expected Output: 2

# Additional test cases
print(s.secondMostFrequentElement([1, 1, 2, 2]))  # Expected Output: 1
print(s.secondMostFrequentElement([1, 1, 1, 2, 2, 3]))  # Expected Output: 2
print(s.secondMostFrequentElement([1, 2, 3]))  # Expected Output: None
print(s.secondMostFrequentElement([1, 1, 1]))  # Expected Output: None
