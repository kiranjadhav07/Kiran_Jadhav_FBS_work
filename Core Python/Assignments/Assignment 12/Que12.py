# Que12....python program to count number of lowercase characters in a string..

# [With Method]
# s=input("Enter a string:")
# count=0
# for i in s:
#     if(i.islower()):
#         count=count+1
# print("Number of lowercase characters=",count)

# [Without Method]
s=input("Enter a string:")
count=0
for i in s:
        if i>'a' and i<'z':
            count=count+1
print("Number of lowercase characters=",count)

 