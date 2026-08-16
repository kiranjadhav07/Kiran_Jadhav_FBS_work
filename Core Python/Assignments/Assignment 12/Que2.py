# Que2...python program to remove the nth Index character from a Non-empty string..

# [Without Method] 
str=input("Enter a string:")
n=int(input("Enter a index:"))
new=""
for i in range(0,len(str)):
    if(i!=n):
        new=new+str[i]
print("Original string=",str)
print("New string=",new)


#  [with Method]

# str=input("Enter a string:")
# n=int(input("Enter a string:"))
# new=str[ :n]+str[n+1: ]
# print("New string=",new)