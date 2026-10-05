#    *
#   * *
#  * * *
# * * * *
n = int(input("Enter the number of rows: "))
for i in range(n): # Loop through each row
    print(" " * (n - i - 1), end="") # Print spaces before stars Spaces decrease as row number increases
    for j in range(i + 1): # Print stars Number of stars increases with each row
        print("*", end=" ")
    print() # Move to the next line