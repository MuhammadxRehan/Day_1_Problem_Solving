# Write a Python program to reverse a string without using built-in functions.


# method 1 
st = "this is a string"
reverse = st[:: -1]
print(reverse)



# method 2
s1 = "working with code"
rev = ''
for ch in s1:
    rev = ch + rev
print(rev)


# method 3
s2 = "i need improvement"
rev2  = ''

i = len(s2) -1

while i >= 0:
    rev2 += s2[i]
    i -= 1

print(rev2)




# method 4
# Note: to reverse the words  

s3 = 'ali is a bignner programer'
words = s3.split()
reverse = ''
for word in words:
    reverse = word + ' ' + reverse
print(reverse.strip())


