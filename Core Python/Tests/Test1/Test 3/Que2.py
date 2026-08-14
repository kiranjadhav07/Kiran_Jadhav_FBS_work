# Que...Write a program to calculate the sum of series where n is input given by user.
# 1/1!+2/2!+3/3!+.....n/n!


n=int(input("Enter n: "))
fact=1
sum=0
for i in range(1,n+1):
        fact=fact*i
        sum=sum+(i/fact)
print("Sum of series =",sum)