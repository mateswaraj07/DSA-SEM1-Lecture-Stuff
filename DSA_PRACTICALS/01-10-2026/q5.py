# Write a program to accept N integers into an array and 
# display the elements in reverse order without changing the original array. 
n = int(input("How many elements do you want in the array: "))
arr = []
print("Enter Elements: ", end=" ")
for i in range(n):
    arr.append(int(input()))

print("Elements in Reverse Order: ", end=" ")
for i in range(n-1, -1, -1): #-1,-1,-1 taken because we want to start from the last index and go to the first index
    print(arr[i], end=" ")
print()