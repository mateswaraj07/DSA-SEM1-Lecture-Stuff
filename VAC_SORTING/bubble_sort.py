# Bubble Sort — Simple Algorithm

# Meaning: Bubble sort compares two adjacent elements and swaps them if they are in the wrong order.

# Algorithm
# Start from the first element.
# Compare two adjacent elements.
# If the first element is greater than the second, swap them.
# Repeat until the largest elements move to the end.
# Continue until the array is sorted.

arr = [13, 46, 24, 52, 20, 25]

for i in range(len(arr)):
    for j in range(len(arr) - 1 - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(arr)