# Write a program to accept N integers into an array and 
# rearrange the elements so that all 0 values are moved to the end while maintaining 
# the relative order of the non-zero elements without new array. 
n = int(input("How many elements do you want in the array: "))
arr = []
print("Enter Elements: ", end=" ")
for i in range(n):
    arr.append(int(input()))
index = 0
for i in range(len(arr)):
    if arr[i]!=0:
        arr[index] = arr[i]
        index += 1
while index < len(arr):
    arr[index]=0
    index += 1
print("Array with 0s at the end: ", arr)
#The logic used here is to maintain an index for the next non-zero element and 
# overwrite the original array with non-zero elements, then fill the rest of the array with zeros.