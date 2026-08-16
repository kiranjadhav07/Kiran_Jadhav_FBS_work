# que8...python program to remove the characters  to odd index values in a string..
str=input("Enter a string:")
new=" "
for i in range(0,len(str)):
    if(i%2==0):
        new=new+str[i]
print("Original list=",str)
print("New list=",new)
