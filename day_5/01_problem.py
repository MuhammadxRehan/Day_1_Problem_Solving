# Write a Python program to write student names into a file.

#  Note : this logic write by my slef 
# this is our name dictionary
stud = {
    'student1':'Rehan' ,
    'student2':'hammad',
    'student3':'Noshad'
}
# in this line we open a file with write mood
file = open('Students.txt','w')
# in this line we write our dictionary in file by converting into a string
file.write(str(stud))
# in this line we close the file 
file.close()



#  this method i improve with LLM 
# with keyword is used to directly close the the file  and
# as keyword used to assign the name to a variable 

with open('Students.txt','w') as file:
    #  we used a for loop on dictionary values not on keys 
    for name in stud.values():
        # in this line ww just print the iteration
        # our file automatically closed because using with keyword  
        file.write(name + '\n')
    



