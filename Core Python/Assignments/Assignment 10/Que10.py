# Que10...Write a program to remove all occurences of a given in the list
li=[10,20,30,20,40,20]
num=int(input("enter a element:"))
new=[]
for i in li:
    if i!=num:
        new=new+[i]
print("Original list:",li)
print("new list:",new)