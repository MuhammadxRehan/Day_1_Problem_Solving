
# Write a Python program to copy contents from one file to another.

with open('Students.txt' ,'r') as f:
    content = f.read()

with open('copyStudents.txt' , 'w') as copy_f:
    copy_f.write(content)
