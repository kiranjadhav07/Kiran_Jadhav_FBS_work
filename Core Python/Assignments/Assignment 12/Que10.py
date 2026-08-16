# Que 10...Python program to take in two  strings and display the larger string without using in built in functions..

s1=input("Enter a string:")
s2=input("Enter a string:")
l1=0
l2=0
for i in s1:
    l1=l1+1
for i in s2:
    l2=l2+1
if(l1>l2):
    print("Larger string:",s1)
elif(l2>l1):
    print("Larger string:",s2)
else:
    print("Both strings are equal:")