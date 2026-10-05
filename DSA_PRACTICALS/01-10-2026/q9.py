# Write a program to count vowels, consonants, digits and special 
# characters in a given string. 
string = input("Enter a string: ")
vowels = 0
consonants = 0
digits = 0
special_characters = 0

for char in string:
    if char.lower() in "aeiou":
        vowels += 1
    elif char.isalpha():
        consonants += 1
    elif char.isdigit():
        digits += 1
    else:
        special_characters += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Special Characters:", special_characters)