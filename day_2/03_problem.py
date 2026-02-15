# Write a Python program to find the largest element in a list.

# method 1 
# this is list of names 
l1 = ['ali' , 'hammad' , 'noshi' , 'asad' ]
# suppose indux number one is largest element
largest  = l1[0]
#  a for loop on list 
for item in l1:
    # comparing lenght of largest element and iteration element 

    if len(item) > len(largest):
        # asinging vaules tio largest 
        largest = item

print(largest)



# method 2 
# list of words 
l2 = ['word','program', 'nothing']
# using max() method to find out elemet 
larg = max(l2, key = len )
print(larg)