# Insertion Sort — Simple Algorithm

# Meaning: Insertion sort takes one element at a time and inserts it into its correct position in the sorted part of the array.

# Algorithm
# Start from the second element.
# Store the current element in key.
# Compare key with the previous elements.
# Shift larger elements one position to the right.
# Insert key into its correct position.
# Repeat until the array is sorted.

arr = [13, 46, 24, 52, 20, 25]

for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j = j - 1
    arr[j + 1] = key
print(arr)