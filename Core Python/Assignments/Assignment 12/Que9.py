# Que9...python program to calculate the number of words and number of caharcters present in a string..

# [ Without Method]
# s=input("Enter a string:")
# countch=0
# countw=1
# for i in s:
#     if(i!=" "):
#         countch=countch+1
#     if(i==" "):
#         countw=countw+1
# print("Number of count=",countch)
# print("Number of countw=",countw)


# [With Method]
s=input("Enter a string:")
word=s.split()
characters=len(s.replace(" ",""))
print("Numbers of words=",len(word))
print("Numbers of characters=",characters)
