# Find all occurrences of substring in a given string.
s1 = input("Enter the main string: ")
s2 = input("Enter the substring to find: ")
count = 0
position = 0
while True:
    position = s1.find(s2, position) # find the substring from the current position
    if position == -1: # if substring is not found, break the loop
        break
    count += 1
    print(f"Found at index: {position}")
    position += 1  # Move one position forward so overlapping substrings are also counted
print(f"Total occurrences of '{s2}': {count}")