#     *
#     *
# * * * * *
#     *
#     *
# Logic:
# Print 7 rows and 7 columns.
# Print '*' when the position is in the middle row or middle column.
# Otherwise print a space.
n = int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(n):
        if i == n//2 or j == n//2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()