# Write a Python program to check password strength.

password = input('Enter your password: ')
#Note 1 
# lines 5 to 8 shows False conditions 
ps_upper = False
ps_lower = False
ps_digit = False
ps_special = False



for ch in password: # for on entered password 

    # Note2: lines 13 to 21 have same logic 

    if ch.isupper(): # checks whether upper or not 
        ps_upper= True # if yes our line 5 condition become True 
    elif ch.islower():  
        ps_lower = True
    elif ch.isdigit():
        ps_digit = True
    else:
        ps_special = True

 #checks all conditions
if len(password) >= 8 and ps_digit and ps_lower and ps_special and ps_upper:
    print('Password is strong') # if True prints this 
else:
    print('Password is week') #if Not prints this 
    