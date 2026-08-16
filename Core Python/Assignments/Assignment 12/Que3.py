# Que3...Python program to detect if two strings are anagrams..

# [With Method]

# str1=input("Enter first string:")
# str2=input("Enter second string:")
# if sorted(str1)==sorted(str2):
#     print("Strings are Anagrams.")
# else:
#     print("Strings are Anagrams.")

# [without Method]

s1=input("Enter first string:")
s2=input("Enter second string:")
counts1=0
counts2=0
if (len(s1) != len(s2)):
    print("Not Anagram")
else:
    for ch in s1:
        for i in s1:
            if ch==i:
                counts1+=1
        for j in s2:
            if ch==j:
                counts2+=1
    if (counts1 == counts2):
        print("Anagrams")
    else:
        print("Not Anagrams")

