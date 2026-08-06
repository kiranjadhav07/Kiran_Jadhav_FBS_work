# Que6...Write a program to find print the following fibonacci series using functions.

def fibonacci(n):
    a=-1
    b=1
    for i in range(n):
        c=a+b
        print(c,end=' ')
        a=b
        b=c
n=int(input("Enter a terms:"))
print("fibonacci series:")
fibonacci(n)