# Write a program to accept a sentence 
# and find the longest and shortest word in a sentence. 
sentence = input("Enter a sentence: ")
words = sentence.split() # it splits the sentence into words
longest_word = ""
shortest_word = words[0] # initialize shortest_word with the first word
for word in words: # loop through each word in the list
    if len(word) > len(longest_word): # check if the current word is longer than the longest_word
        longest_word = word # update longest_word
    if len(word) < len(shortest_word): # check if the current word is shorter than the shortest_word
        shortest_word = word # update shortest_word
print(f"Longest word: {longest_word}")
print(f"Shortest word: {shortest_word}")