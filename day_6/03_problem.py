# Write a Python program to count uppercase and lowercase letters in a string.

# this line 4 is our string 
st = 'im Learning Python which is a Computer Language'

count_upper = 0 # counter for uppercase letters

count_lower = 0 # counter for lowercase letter

for ch in st:  # A for loop on string 
    if ch.isupper(): # checks whether uppercase or not 
        count_upper += 1 # if True increment 1
    else: 
        count_lower += 1 # it counts lowercase letter 
# prints the final output 
print(f'There are {count_upper} uppercase letters and {count_lower} lowercase letters.')