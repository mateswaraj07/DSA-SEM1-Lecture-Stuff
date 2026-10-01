#  Write a program to accept N integers into an array and calculate and display the sum of all the elements. 
n = int(input("How many elements do you want in the array: "))
arr = []
print("Enter Elements: ")
for i in range(1,n+1):
    e = int(input())
    arr.append(e)
print("Elements: ",arr)
sum = 0
for i in range(1,n+1):
    sum += i
print("Sum of elements: ",sum)