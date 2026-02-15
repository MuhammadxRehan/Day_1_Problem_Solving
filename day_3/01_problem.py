# Write a Python program to print a square star pattern.



def pattern(n):
    for i in range(n):
        for j in range(n):
            print("*",end=' ')
        print()
        
n = int(input("Pattern number: "))
pattern(n)