# Que14...Python program to count the occurence of the word in string..
s=input("Enter a string:")
words=s.split()
for i in range(len(words)):
    count=0
    if(words[i] not in words [:i]):
        for j in words:
            if words[i]==j:
                count=count+1
        print(words[i],'=',count)