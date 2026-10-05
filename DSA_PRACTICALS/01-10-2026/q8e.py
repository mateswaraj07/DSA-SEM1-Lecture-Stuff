# 1 0 1 0 1
# 0 1 0 1 0
# 1 0 1 0 1
# 0 1 0 1 0
# 1 0 1 0 1
# Logic:
# Print a 5 x 5 pattern.
# If the sum of row and column indexes is even,
# print 1; otherwise print 0.
# This creates an alternating pattern.
n = int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()