# Write a Python program to count the number of words in a sentence.


sen = 'this is a line of code'

temp = sen.split()
count = 0
for i in temp:
    count += 1

print(count)