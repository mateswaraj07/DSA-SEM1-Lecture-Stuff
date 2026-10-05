#   *
#  * *
# *   *
#  * *
#   *
# Logic:
# The diamond has 9 rows.
# First, print the upper half.
# Then print the lower half.
# Spaces are used to center the stars.
n = int(input("Enter the number of rows: "))
# Upper half
for i in range(n//2 + 1):  # Loop through the upper half rows
    # Print spaces before the stars
    for j in range(n//2 - i): 
        print(" ", end=" ")

    # Print stars only at the boundary
    if i == 0:
        print("*")
    else:
        print("*", end=" ")
        for j in range(2 * i - 1):
            print(" ", end=" ")
        print("*")

# Lower half
for i in range(n//2 - 1, -1, -1):
    # Print spaces before the stars
    for j in range(n//2 - i):
        print(" ", end=" ")

    # Print stars only at the boundary
    if i == 0:
        print("*")
    else:
        print("*", end=" ")
        for j in range(2 * i - 1):
            print(" ", end=" ")
        print("*")