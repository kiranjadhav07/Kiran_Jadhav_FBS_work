#Que5...WAP to check the triangle is equilateral,isosceles or scalene


FS=int(input("Enter a first side of:"))
SS=int(input("Enter a Secod side of :"))
TS=int(input("Enter a Third side of:"))
if FS==SS and SS==TS:
    print("Equilateral Triangle")
elif(FS==SS or SS==TS or TS==FS):
    print("Isoceles Triangle")
else:
    print("Scalene Triangle")


