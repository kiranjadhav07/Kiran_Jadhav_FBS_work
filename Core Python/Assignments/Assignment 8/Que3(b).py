#Que3...WAP to find sum of following series using functions 
   
    # (b)..sum of factorial  1!+2!+3!+_ _ _ _+n!

def sumFact(n):
    fact=1
    sum=0
    for i in range (1,n+1):
        fact*=i
        sum+=fact
    return sum
n=int(input("enter n:"))
res=sumFact(n)
print("sum of factorial=",res)