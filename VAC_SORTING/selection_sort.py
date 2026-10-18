# Selection Sort — Simple Algorithm

# Meaning: Selection sort finds the smallest element and places it at the correct position.

# Algorithm
# Start from the first element.
# Find the smallest element in the unsorted part.
# Swap it with the first element of the unsorted part.
# Repeat until the array is sorted.
# arr = [13, 46, 24, 52, 20, 13]

arr = [13, 46, 24, 52, 20, 25]

for i in range(len(arr)):
    min_index = i

    for j in range(i + 1, len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j

    arr[i], arr[min_index] = arr[min_index], arr[i]
    
print(arr)