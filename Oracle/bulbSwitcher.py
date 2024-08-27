# Problem Statement: Bulb Switcher (Inclusive Range)
# You are given a series of operations where each operation toggles the state of a range of bulbs. Initially, all bulbs are off. Each operation specifies a range of bulbs, and for each bulb within that range (including both the starting and ending indices), its state is toggled (i.e., if the bulb is off, it is turned on, and if it is on, it is turned off).

# Your task is to determine how many bulbs remain on after performing all the toggle operations.

# Input:
# A list of operations. Each operation is represented as a pair [left, right], where:
# left is the starting index of the range (1-based index).
# right is the ending index of the range (inclusive).
# The number of bulbs is determined by the maximum right value across all operations.
# Output:
# An integer representing the number of bulbs that are on after all operations.


def bulbSwitcher():
    update = [
        [2, 4],
        [3, 6],
        [1, 3]
    ]
    n = max([interval[1] for interval in update])  # Find the maximum bulb index
    
    arr = [0] * (n + 1)

    for interval in update:
        left, right = interval
        arr[left - 1] += 1
        arr[right] -= 1

    count = 0
    for i in range(n):
        if i > 0:
            arr[i] += arr[i - 1]  # Calculate cumulative sum
        if arr[i] % 2 == 1:
            count += 1

    print(count)

bulbSwitcher()
