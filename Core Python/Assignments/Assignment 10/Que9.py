# Que9... write a program having  n number of elements in the list and find out even and odd elemnts in that
#  list and create two seprate lists which will have even  elements and other will have odd elements.
n=int(input("Enter number of elements:"))
li=[]

for i in range(n):
    num=int(input("Enter a element:"))
    li=li+[num]
even=[]
odd=[]
for j in range(0,len(li)):
    if(li[j]%2==0):
        even=even+[li[j]]
    else:
        odd=odd+[li[j]]
print("Original list:",li)
print("Even list:",even)
print("Odd list:",odd)