# Que1...python program to replace all occuerence of 'a' with '$' in a string..

# [Without Method]
str=input("enter a string:")
new=""
for i in str:
    if i=='a':
        new=new+'$'
    else:
        new=new+i
print("Original string=",str)
print("New string=",new)


# [with method]
# str=input("enter a string:")
# new=str.replace('a','$')
# print("Original string=",str)
# print("new string=",new)