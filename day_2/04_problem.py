# Write a Python program to remove duplicate elements from a list.

# method 1
l1 = ['dog' , 'cat', 'cow' , 'dog']
final  = []
for item in l1:
    if item not in final:
        final.append(item)
print(final)


# method 2 

name = ['ali' ,'rehan' ,'hami']

final = list(set(name))
print(final)