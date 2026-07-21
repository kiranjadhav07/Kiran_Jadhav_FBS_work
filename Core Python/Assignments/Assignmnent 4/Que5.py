#QUE5...WAP to print fibonacci series up to n terms

n =int(input("Enter a number :"))
a=-1
b=1
for i in range (n):
    c=a+b
    print(c)
    a=b
    b=c
