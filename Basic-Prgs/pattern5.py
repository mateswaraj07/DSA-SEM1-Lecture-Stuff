#   *
#  * *
# *   *
#  * *
#   *

n = int(input("Enter the number of rows: "))
# ---------------- UPPER HALF ----------------
for i in range(n): # Loop from 0 to n-1
    print(" " * (n - i - 1), end="") # Print spaces before stars As i increases, spaces decrease
    for j in range(i + 1):   # Loop to print stars and spaces
        if j == 0 or j == i: 
            print("*", end=" ")  # Print * at the first and last position
        else:
            print(" ", end=" ")  # Print space between the two stars
    print() # Move to the next line
# ---------------- LOWER HALF ----------------
for i in range(n - 2, -1, -1):  # Loop from n-2 down to 0 We start from n-2 to avoid repeating the middle row
    print(" " * (n - i - 1), end="") # Print spaces before stars As i decreases, spaces increase
    for j in range(i + 1):  # Loop to print stars and spaces
        if j == 0 or j == i:
            print("*", end=" ") # Print * at the first and last position
        else:
            print(" ", end=" ") # Print space between the two stars
    print()  # Move to the next line