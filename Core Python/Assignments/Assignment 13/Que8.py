# Que8...Python program to count frequency of words appearing in a string using a dictionary.

s=input("enter string:")
words=s.split()
d={}
for word in words:
    if word in d:
        d[word]=d[word]+1
    else:
        d[word]=1
print("word frequency=",d)