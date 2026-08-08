#Que2... Write a program to check if given numbers is Armstrong or not using recursive
def armstrong(num):
    if num>0:
        digit =num%10
        return digit ** count + armstrong(num//10)
    else:
        return 0
num=int(input("Enter a number:"))
count=len(str(num))
res=armstrong(num)
if(res==num):
    print(f"{num} is armstrong number.")
else:
    print(f"{num} is  not armstrong number.")
