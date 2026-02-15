# Write a Python program to find the longest word in a sentence.


sentence = 'life become easy when thinking is big ' # this is our string 
sentence = sentence.split() # split function convert string into a list 
longest = sentence[0] # lets suppose first indux is longest 

for ch in sentence: # for on sentence with split()
    if len(ch) > len(longest): # it compare the length of items
        longest = ch  # if longest is less values will change 

print(longest)  # print final output 

