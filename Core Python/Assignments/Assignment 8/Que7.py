#Que7...Write a program find sum of digits of a...
def sumDigits(num):
    sum=0
    while(num>0):
        d=num%10
        sum=sum+d
        num=num//10
    return sum
num=int(input("enter a number:"))
print ("sum of digits=",sumDigits(num))