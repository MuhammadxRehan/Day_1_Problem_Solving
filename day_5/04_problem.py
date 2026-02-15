# Write a Python program to search a word in a file.
# in this line we open a file 
with open('students.txt' , 'r') as a:
    # in this line we read the content of file 
    content =a.read()
    # this is name we wants to search 
    name = 'Rehan'
    # in this line we set a conditonal constructs
    if name.lower() in content.lower():
        # if True print this line 
        print('Word in file.')
    else:
        # if False print this line 
        print('word not in file.')