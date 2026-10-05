# * * * * *
# *       *
# *       *
# *       *
# * * * * *
# Logic:
# Print a 5 x 5 square.
# '*' is printed on the first/last row
# or first/last column.
# This creates a hollow square.
n = int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1: #this condition checks if we are on the first or last row, or first or last column
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()