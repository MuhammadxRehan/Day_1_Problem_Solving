# Write a Python program to check whether two strings are anagrams

st1 = 'code makes life easy'
st2 = 'fee say likes madeco'

st1 = st1.replace(' ' ,'').lower()
st2 = st2.replace(' ', '').lower()
if sorted(st1) == sorted(st2):
    print('these string are anagrams.')
else:
    print('these string are not anagrams.')
