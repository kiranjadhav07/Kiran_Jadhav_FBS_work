#Que3...WAP to find sum of following series using functions

     #(c)1^1+2^2+3^3+_ _  _ _ +n^n

def powerSum(n):
    sum=0
    for i in range(1,n+1):
        sum+=i**i
    return sum
n=int(input("enter n:"))
res=powerSum(n)
print("sum of Power=",res)

