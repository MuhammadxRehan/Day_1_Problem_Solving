# Write a Python program to print the multiplication table of a given number.


def table(num):
    for i in range(1,11):
        print(f'{num} X {i} = {num*i}')

num = int(input('Enter a number: '))
table(num)