#Que12...WAP to check if given 3 digit number is palindrome or not...

num=int(input("Enter Three Digit Number:"))
temp=num
d1=num%10
num=num//10
d2=num%10
numm=num//10
d3=num%10
num=num//10
rev=d1*100+d2*10+d3
if(rev==temp):
    print("Number is palindrome")
else:
    print("Number is not palindrome")