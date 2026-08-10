# Que7....Write a program to create a new list from existing list which contains cube of each number of list..

li=[1,2,3,4,5]
new=[]
for i in range (0,len(li)):
    new=new+[li[i]**3]
print("Orginal list=",li)
print("New list=",new)