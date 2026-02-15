# Write a Python program to read a file and count lines.

with open('Students.txt', 'r') as f:
    names = f.read()
    lines = f.readlines()

    print(names,f'number of lines:{len(lines)}')