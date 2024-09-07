def maxUnitsUsingHashMap(boxes, unitsPerBox, truckSize):
    # Step 1: Create a HashMap (dictionary) to store unitsPerBox as keys and boxes as values
    hashMap = {}
    for i in range(len(boxes)):
        hashMap[unitsPerBox[i]]=boxes[i]

    sorted_pairs = sorted(hashMap.items(), key = lambda x:x[0], reverse=True)

    remaining_truck_size = truckSize
    for units,num_boxes in sorted_pairs:
        min(remaining_truck_size,)

# Example usage
boxes = [1, 2, 3]
unitsPerBox = [3, 2, 1]
truckSize = 3

print(maxUnitsUsingHashMap(boxes, unitsPerBox, truckSize))  # Output: 7
