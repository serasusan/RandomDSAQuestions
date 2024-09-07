def count_divisible_triplets(arr, d):
    n = len(arr)
    count = 0
    
    # Iterate over the first two elements of the triplet
    for i in range(n):
        for j in range(i + 1, n):
            # Create a hashmap to store the frequency of elements between a[i+1] and a[j-1]
            freq = {}
            
            # Build the hashmap for elements between i+1 and j-1
            for k in range(i + 1, j):
                if arr[k] in freq:
                    freq[arr[k]] += 1
                else:
                    freq[arr[k]] = 1
            
            # Sum of the fixed two elements
            fixed_sum = arr[i] + arr[j]
            
            # Calculate the needed value to make the total sum divisible by d
            needed_value = (d - (fixed_sum % d)) % d
            
            # Check if the needed value is present in the hashmap
            if needed_value in freq:
                count += freq[needed_value]

    return count

# Example usage
arr = [3, 3, 4, 7, 8]
d = 5
result = count_divisible_triplets(arr, d)
print(result)  # Output: 3
