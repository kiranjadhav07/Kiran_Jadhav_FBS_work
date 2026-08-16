# Que5...Python program to count the number of vowles in a string..

s=input("Enter a string:")
count=0
for i in s:
    if i in"aeiouAEIOU":
        count+=1
print("Number of vowel=",count)