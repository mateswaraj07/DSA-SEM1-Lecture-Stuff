# Write a program to accept N integers into an array and 
# find and display the largest element, second largest element, 
# smallest element, second smallest element present in the array. 
n = int(input("How many elements do you want in the array: "))
arr = []
print("Enter Elements: ", end=" ")
for i in range(n):
    arr.append(int(input()))
print("Elements: ",arr)
min = arr[0]
smin = arr[0]
max = arr[0]
smax = arr[0]
for num in arr:
    if num < min:
        smin = min
        min = num
    if num > max:
        smax = max
        max = num
print("Maximum: ", max)
print("Minimum: ",min)
print("Second Maximum: ", smax)
print("Second Minimum: ",smin)

# n = int(input("How many elements do you want in the array: "))

# arr = []

# print("Enter Elements:")
# for i in range(n):
#     arr.append(int(input()))

# print("Elements:", arr)

# min = arr[0]
# max = arr[0]
# smin = None
# smax = None

# for num in arr[1:]:
#     # Find minimum and second minimum
#     if num < min:
#         smin = min
#         min = num
#     elif num != min and (smin is None or num < smin):
#         smin = num

#     # Find maximum and second maximum
#     if num > max:
#         smax = max
#         max = num
#     elif num != max and (smax is None or num > smax):
#         smax = num

# print("Maximum:", max)
# print("Second Maximum:", smax)
# print("Minimum:", min)
# print("Second Minimum:", smin)