# Que13... Python program to count  number of digits and letter is a string..

# [Without Method]
# s=input("Enter string:")
# countd=0
# countl=0
# for i in s:
#     if i.isdigit():
#         countd=countd+1
#     elif i.isalpha():
#         countl=countl+1
# print("Number of digits =",countd)
# print("Number of letters=",countl)

# [With Method]
s=input("Enter string: ")
countd=0
countl=0
for i in s:
    if i>='0' and i<='9':
        countd=countd+1
    elif(i>='a'and i<='z') or (i>='A'and i<="Z"):
        countl+=1
print("Number of digits=",countd)
print("Number of letters=",countl)
