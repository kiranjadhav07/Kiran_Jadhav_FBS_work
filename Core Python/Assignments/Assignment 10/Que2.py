#Que2....write a program  to find maximum and minimum element in a list.
li=[52,33,93,77,15,7]
max=li[0]
min=li[0]
for i in range(1,len(li)):
    if li[i]>max:
        max=li[i]
    if li[i]<min:
        min=li[i]
print("Maximum element=",max)
print("Minimum element=",min)