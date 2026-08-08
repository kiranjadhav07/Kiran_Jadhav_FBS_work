#  Que4...Write a program to find sum of n numbers using recursion

def sumNum(n):
    if n>0:
        return n+ sumNum(n-1)
    else:
        return 0
n=int(input("Enter a number:"))
res=sumNum(n)
print("Sum of Numbers=",res)