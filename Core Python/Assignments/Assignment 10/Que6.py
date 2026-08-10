# Que6...Write a program remove duplicates from the list

li=[10,20,10,30,20,40]
new=[]
for i in li:
    if i not in new:
        new=new+[i]
print(new)