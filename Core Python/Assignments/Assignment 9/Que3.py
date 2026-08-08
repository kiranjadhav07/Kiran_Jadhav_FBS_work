# Que3... Write a program to reverse a given number using recursive function
def reverse(num,rev):
    if num>0:
        d=num%10
        rev=rev*10+d
        return reverse(num//10,rev)
    else:
        return rev
n=int(input("Enter a number:"))
res=reverse(n,0)
print(res)