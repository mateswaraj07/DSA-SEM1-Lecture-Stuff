# Write a program to accept N integers into an array and search for a given number. 
# Display an appropriate message indicating whether the number is present in the array or not and 
# also display its position. 
n = int(input("How many elements do you want in the array: "))
arr = []
print("Enter Elements: ", end=" ")
for i in range(n):
    arr.append(int(input()))
target = int(input("Enter the number to search: "))
found = False
for i in range(n):
    if arr[i] == target:
        found = True
        print(f"Number {target} is present at position {i+1}.")
        break
if not found:
    print(f"Number {target} is not present in the array.")