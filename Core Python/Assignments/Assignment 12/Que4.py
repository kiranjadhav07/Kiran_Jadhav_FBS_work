# Que4...Python program to from a new string  where the first character have been exchanged..

#  [Without Method]
s=input("Enter string:")
new=s[len(s)-1]
for i in range(1,len(s)-1):
    new=new+s[i]
new=new+s[0]
print("Original list=",s)
print("New list=",new)

# [with Method]
# s=input("Enter String:")
# new=s[len(s)-1]+s[1:len(s)-1]+s[0]
# print("new string=",new)