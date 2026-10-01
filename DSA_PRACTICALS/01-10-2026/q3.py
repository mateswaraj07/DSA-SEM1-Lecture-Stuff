# Write a program to accept N integers into an array and 
# count and display the number of even and odd elements present in the array. 
n = int(input("How many elements do you want in the array: "))
arr = []
print("Enter Elements: ", end=" ")
for i in range(n):
    arr.append(int(input()))
even = 0
odd = 0
for num in arr:
    if num % 2 == 0:
        even += 1
    else: 
        odd += 1
print("Number of Even Elements: ", even)
print("Number of Odd Elements: ", odd)