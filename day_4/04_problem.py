# Write a Python program to separate even and odd numbers from a list.

num = [32,51,12,5,1,78,8,44]
even = []
odd = []

for i in num:
    if i% 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print(even,odd)