# Write a Python program to check whether a number is a perfect number.

num = int(input('Enter a number: ')) # input from user

sum = 0  # sum always zero at first 

for i in range(1, num): # for loop on range given num 
    if num% i == 0: # checks  proper divisors
        sum += i # increment iteration item in sum 

if sum == num: # checks whether sum and number ar equal or not 
    print(f'{num} is a Perfect Number')  # print perfect number
else:
    print(f'{num} is not a Perfect Number') #prints none perfect number
    
 


