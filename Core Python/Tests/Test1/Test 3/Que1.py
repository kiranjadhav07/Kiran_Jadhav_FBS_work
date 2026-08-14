# QUE1 write a program to print first n numbers.

n=int(input("Enter n: "))
count=0
num=2
print(f"first{n} prime numbers")
while count<n:
    c=0
    for i in range(2,num):
        if num%i==0:
            break
    else:
        print(num)
        count=count+1
    num=num+1