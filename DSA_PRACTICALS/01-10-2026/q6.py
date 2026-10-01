# Write a program to accept N integers into an array and 
# create a new array containing only the unique elements, removing all duplicate values. 
n = int(input("How many elements do you want in the array: "))
arr = []
print("Enter Elements: ", end=" ")
for i in range(n):
    arr.append(int(input()))
new = []
print("Original Array: ", arr)
for i in arr:
    if i not in new:
        new.append(i)
print("Array with Unique Elements: ", new)