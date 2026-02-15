# Write a Python program to check whether a number is an Armstrong number.


n= int(input("Enter your number: "))

temp = n
digit = len(str(n))
sum = 0 

while temp > 0 :
    digit = temp % 10 
    sum = sum + digit**digit
    temp = temp // 10


if sum == n:
    print("True")
else:
    print("False")