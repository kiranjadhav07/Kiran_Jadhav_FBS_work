# Que1.... write program to find area and perimetere of following figure( accept the length, breadth, radius from user.)

l=int(input("Enter a length:"))
b=int(input("Enter a breadth:"))
r=int(input("enter a raduis:"))
area = (l * b) + (3.14 * r * r) / 2
perimeter = (2 * l) + b + (3.14 * r)
print("Area =", area)
print("Perimeter =", perimeter)