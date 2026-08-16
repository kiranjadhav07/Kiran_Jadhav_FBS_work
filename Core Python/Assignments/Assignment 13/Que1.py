# Que1...python program to  Add a key-value pair to the dictionary.
  

# [without Method]
# d={'id':101,'name':'kiran','age':21}
# key=input("enter key:")
# value=input("Enter value:")
# d[key]=value
# print("updated dictionary=",d)

# [with Method]
d={'id':101,'name':'kiran','age':21}
key=input("enter key:")
value=input("Enter value:")
d.update({key:value})
print("updated dictionary=",d)

