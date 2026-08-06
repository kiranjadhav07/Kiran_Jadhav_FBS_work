#Que2...WAP a program to calculate ara of circle

def areaCircle(r):
    return 3.14*r*r
radius=int(input("Enter a radius:"))
res=areaCircle(radius)
print(f'Area of circle={res}')