# Que11...Write a program to print all numbers which are divisible by m  and n in the list..
li=[28,21,36,30,44,48]
m=int(input("Enter a number m:"))
n=int(input("Enter a number n:"))
print("Numbers divisible by",m,"and",n)
for i in range(0,len(li)):
    if li[i]%m==0 and li[i]%n==0:
        print(li[i])

