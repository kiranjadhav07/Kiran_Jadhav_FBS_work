# Que12...write a program to create three lists of numbers theirs squares and cubes

li=[2,5,7,9,10]
square=[]
cube=[]
for i in range(0,len(li)):
    square=square+[li[i]**2]
    cube=cube+[li[i]**3]
print("Original list=",li)
print("squares=",square)
print("cubes=",cube)