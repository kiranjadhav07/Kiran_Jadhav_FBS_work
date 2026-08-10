# Que5....Accept a number from user and check if this element is present in the list or not.also tell how many times is it present in the list.

li=[10,20,30,10,40,50,60,10]
n=int(input("enter a number:"))
count=0
for i in range(0,len(li)):
    if li[i]==n:
        count=count+1
if count>0:
    print("Number is present.")
    print("How many times present=",count)
else:
    print("Element not present")