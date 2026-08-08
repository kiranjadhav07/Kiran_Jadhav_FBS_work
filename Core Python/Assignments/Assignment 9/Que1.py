# Que1... Write a program  to find sum of following series recursive functions.
def fact(n):
    if (n>0):
        return n*fact(n-1)
    else:
        return 1
def sum_fact(n):
    if(n>0):
        return fact(n)+sum_fact(n-1)
    else:
        return 0
n=3
res=sum_fact(n)
print(res)
