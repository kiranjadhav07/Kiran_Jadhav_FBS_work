#Que6...Write a program to print first n prime numbers.

n = int(input("Enter the value of n: "))
count = 0
num = 2
print(f"First {n} prime numbers:")
while count < n:
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)
        count += 1
    num += 1