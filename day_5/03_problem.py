# Write a Python program to append text to an existing file.
name  = 'izan'
with open('Students.txt','a') as file:
    file.write(name)
