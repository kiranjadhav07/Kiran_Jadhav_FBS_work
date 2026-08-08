#Que7... Write a program to find sum of digits using recursion

def sumDigit(num):
    if num>0:
        d=num%10
        num=num//10
        return d + sumDigit(num)
    else:
        return 0
num=int(input("Enter a number:"))
res=sumDigit(num)
print(res)