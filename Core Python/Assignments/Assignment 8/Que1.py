#Que1...WAP to calculate Area of Rectangle

def AreaRectangle(l,b):
    return l*b
length=int(input("Enter a length:"))
breadth=int(input("Enter a breadth:"))
res=AreaRectangle(length,breadth)
print(f'Area of Rectangle={res}')
