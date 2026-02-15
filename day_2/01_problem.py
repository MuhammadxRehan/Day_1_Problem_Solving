# Write a Python program to count vowels in a string.

#  method 1
# this line is a string
s1 = "this is a book"
# this line show the count for vowels 
count = 0
# for loop checks the charachters of string with converting  string into lower case 
for  i in s1.lower():
    # these below lines shows that if iteration is vowels  add count
    if "a" in i:
        count += 1
    elif "e" in i:
        count += 1
    elif "i" in i:
        count += 1
    elif "o" in i:
        count += 1
    elif "u" in i:
        count +=1 
#print the final output  
print(count)



# method 2 
# this is a string 
s2 = 'how are you?'
# here is list of vowels 
vowels = ['a','e','i','o','u']
# right now count starts from zero
count = 0
# this for loop apply on given string and converts string into lowercase 
for ch in s2.lower():
    #this line checks whather vowels in iteration if there add a count 
    if ch in vowels:
        count +=1
print(count)



# method 3

s3 ='Ali is author of this program.'
count= 0
# a for loop used on vowels string 
for ch in 'aeiou':
    # we used count method 
    count += s3.lower().count(ch)
print(count)


#  method 4 
# method 4 , and 2 are have same logic but their syntax is change 
# the syntax is little bit advance 
s4 = 'this is another method'
count = sum(1 for ch in s4.lower() if ch in 'aeiou')
print(count)