#     *
#     *
# * * * * *
#     *
#     *
n = int(input("Enter the number of rows: "))
for i in range(n):  # Loop through rows
    for j in range(n): # Loop through columns
        if i == n // 2 or j == n // 2:
            print("*", end=" ") # Print * in the middle row or middle column
        else:
            print(" ", end=" ")   # Otherwise print space
    print() # Move to next row