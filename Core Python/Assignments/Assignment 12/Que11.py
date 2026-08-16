# Que11...python program to replace every blank space with hypen in string..

s=input("Enter a string:")
new=""
for i in s:
    if (i==" "):
        new=new+'-'
    else:
        new=new+i
print("New string=",new)
