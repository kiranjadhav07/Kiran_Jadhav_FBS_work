#Que6... Write a program to print fibonacci series using recursion

def fibonacci(n,a,b):
    if n>0:
        c=a+b
        print(c,end=' ')
        return fibonacci(n-1,b,c)
n=int(input("Enter a number:"))
print("fibonacci series")
fibonacci(n,-1,1)