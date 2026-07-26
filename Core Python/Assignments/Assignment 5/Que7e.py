#Que7.(e)..... x - x2/3 + x3/5 - x4/7 + .... to n terms


x=int(input("enter the number:"))
n=int(input("enter the ending value:"))
dem=1
sign=1
sum=0
for i in range(1,n+1):
    sum=sign*(x**i)/dem
    dem=+2
    sign*=-2
print("sum=",sum)
