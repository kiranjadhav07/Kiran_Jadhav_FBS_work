#Que1.. python program to put Even an odd elemnts of a list into two different lists.

li=[20,31,32,43,54,65]
even=[]
odd=[]
for i in range(0,len(li)):
    if li[i]%2==0:
        even=even+[li[i]]
    else:
        odd=odd+[li[i]]
print("Original list=",li)
print("Even list=",even)
print("Odd list=",odd)