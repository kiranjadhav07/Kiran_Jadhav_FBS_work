#Que8... Write a program to check wheather a number is prime or not using recursive

def prime(num,i):
    if(i==num):
        return True
    if(num%i==0):
        return False
    return prime(num,i+1)
num=int(input("Enter number:"))
if num>0:
    res=prime(num,2)
    if(res):
        print("Number is prime")
    else:
        print("Number is prime")
else:
    print("Number is not  prime")