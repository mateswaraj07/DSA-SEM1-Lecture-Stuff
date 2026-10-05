#       A
#     A   C
#   A       E
# A B C D E F G
n = int(input("Enter the number of rows: "))
for i in range(n):    # Loop for each row
    print("  " * (n - i - 1), end=" ")   # Print spaces before the pattern
    for j in range(2 * i + 1):    # Loop to print characters/spaces in each row
        if i == n - 1:  
            print(chr(65 + j), end=" ")   # If it is the last row, print all alphabets
        elif j == 0 or j == 2 * i:
            print(chr(65 + j), end=" ")  # Print alphabet at the first and last position
        else:
            print(" ", end=" ")  # Print spaces between first and last alphabet
    print() # Move to the next line