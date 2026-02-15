# Write a Python program to generate a random password.
  


# we import random and string modules 
import random , string
            
length = 10 # set the password length

#line 10  use and concatenate all characters
all_chars = string.ascii_letters + string.digits + string.punctuation

password = '' # password with empty string

for i in range(10): # a for loop on password length range
    
    password += random.choice(all_chars) # increment password with random choices

print(f'Generated password:{password}') # print the final output 