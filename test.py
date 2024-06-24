# def custom_sort(arr):
#     # Step 1: Sort the array based on the 1st index (column 1)
#     sorted_arr = arr[arr[:, 1].argsort()]
    
#     # Step 2: Check for adjacent pairs with difference <= 5 in 1st index
#     i = 0
#     while i < len(sorted_arr) - 1:
#         j = i + 1
#         while j < len(sorted_arr) and sorted_arr[j, 1] - sorted_arr[i, 1] <= 5:
#             j += 1
        
#         #this checks till threshold is > 5
        
#         # If we found a group, sort it based on the 0th index
#         if j - i > 1:
#             sorted_arr[i:j] = sorted_arr[i:j][sorted_arr[i:j, 0].argsort()]
        
#         i = j
    
#     return sorted_arr
