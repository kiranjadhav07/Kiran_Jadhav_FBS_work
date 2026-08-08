#Que9... Write a program to calculate the m to the power n using recursion

def power(m,n):
    if n>0:
        return m*power(m,n-1)
    else:
        return 1
m=int(input("Enter the value of m : "))
n=int(input("Enter the value of n : "))
res=power(m,n)
print(f'{m} raised to the power {n} = {res}')