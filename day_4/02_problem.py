# Write a Python program to count frequency of each character in a string.

# #  A simple method for single character
# # this is our string
# st = 'this is string'
# # this is our character wanted to count its frequency
# char = 'i'
# # count alwasys starts from zero 
# count = 0
# # a for loop on our string 
# for i in st:
#     # this line check the character 
#     if char in i:
#         # then add one count 
#         count += 1
# # this line print the final count 
# print(count)


# # using dictionary 
# # this our string
# st2 = 'we are working with string'
# # this an empty dictionary
# freq = {}
# # a for loop on string
# for i in st2:
#     # if character in dictionary 
#     if i in freq:
#         # then charecter valued added on time 
#         freq[i] +=1
#     # these used to set character in dinctionary
#     else:
#         freq[i] =1
# # we print the final output
# print(freq)



# another one method 
# this is string 
st3 = 'working with string'
# this is empty string
checked = ''
# a for loop on main string

for ch in st3:
    if ch not in checked:
        print(ch , ':', st3.count(ch))
    checked += ch

print(checked)
