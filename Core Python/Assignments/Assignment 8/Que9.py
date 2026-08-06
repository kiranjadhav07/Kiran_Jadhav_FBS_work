#Que9...Write a program to check entered number is palindrome or not.
def chkPalindrome(num):
    temp=num
    rev=0
    while(temp>0):
        d=temp%10
        rev=rev*10+d
        temp//=10
    if(rev==num):
        print(f'{num} is palindrome')
    else:
        print(f'{num} is not  palindrome')
num=int(input("enter a number:"))
chkPalindrome(num)