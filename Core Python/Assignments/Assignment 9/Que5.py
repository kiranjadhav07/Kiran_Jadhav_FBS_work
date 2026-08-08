#Que5... write a program to find factorial using

def factorial(n):
    if(n>0):
        return n* factorial(n-1)
    else:
        return 1
n=int(input("Enter a number:"))
res=factorial(n)
print(res)