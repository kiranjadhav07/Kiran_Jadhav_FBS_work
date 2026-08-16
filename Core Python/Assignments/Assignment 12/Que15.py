# Que15...python program to find larger string without usin built in function.

# [without Method]
# s1=input("Enter a string 1:")
# s2=input("Enter a string2:")
# count1=0
# count2=0
# for i in s1:
#     count1+=1
# for i in s2:
#     count2+=1
# if(count1>count2):
#     print("Larger string=",s1)
# elif(count2>count1):
#     print("Larger string=",s2)
# else:
#     print("Both strings are equal ")

# [With Method]
n=int(input("Enter a number of string: "))
larger=""
for i in range(n):
    s=input("enter a string:")
    count=0
    for i in s:
        count=count+1
        larger_count=0
        for j in larger:
            larger_count=larger_count+1
        if (count>larger_count):
            larger=s
print("Larger string:",larger)