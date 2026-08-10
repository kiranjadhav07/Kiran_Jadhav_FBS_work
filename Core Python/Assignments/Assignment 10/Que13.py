# Que13...write a program to print list after removing even numbers..

li=[20,23,25,28,26,13]
new=[]
for i in range(len(li)):
    if li[i]%2!=0:
        new=new+[li[i]]
print("Original list=",li)
print("List after removing even numbers=",new)