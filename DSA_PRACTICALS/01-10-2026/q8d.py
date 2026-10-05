#         1
#       1 2 1
#     1 2 3 2 1
#   1 2 3 4 3 2 1
# 1 2 3 4 5 4 3 2 1
# Logic:
# Print 5 rows.
# Each row contains numbers increasing toward the middle
# and then decreasing.
# Example: 1 2 3 2 1
n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):  # Loop through rows

    # Print spaces to center the pyramid
    for j in range(n - i): # Loop through spaces
        print("  ", end="")

    # Print increasing numbers
    for j in range(1, i + 1): # Loop through increasing numbers
        print(j, end=" ")

    # Print decreasing numbers
    for j in range(i - 1, 0, -1): # Loop through decreasing numbers
        print(j, end=" ")

    print()