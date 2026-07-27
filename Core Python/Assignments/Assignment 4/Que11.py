# Strong number
num=int(input("Enter Number:"))
temp=num
sum=0
while(num>0):
    d=num%10
    fact=1
    for i in range(1,d+1):
        fact*=i
    sum=sum+fact
    num=num//10
if (sum==temp):
    print(f'{temp} is a strong number')
else:
    print(f'{temp}is not a strong number')
