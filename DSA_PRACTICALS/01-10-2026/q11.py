# Write a program to accept a sentence and display by 
# reversing words in a sentence. 
# Ex. “the sky is blue” => “eht yks si eulb”
sentence = input("Enter a sentence: ")
words = sentence.split() # it slits the sentence into words
reverse = [] # list to store the reversed words
for word in words: # loop through each word in the list
    reverse.append(word[::-1]) # it reverses each word and appends to the list
reversed_sentence = ' '.join(reverse) # it joins the reversed words with a space in between to form the final sentence
print("Reversed sentence:", reversed_sentence)