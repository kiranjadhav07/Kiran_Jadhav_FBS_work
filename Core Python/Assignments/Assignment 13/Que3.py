# Que3...Python program to check if a given key exists in a dictionary or not.

# [Without Method]
# d={'id':101,'name':'kiran','age':21,'city':'satara'}
# key=input("enter a search key:")
# if(key in d):
#     print("key already exist")
# else:
#     print("key does not in dictionary")


# [with Method]
d={'id':101,'name':'kiran','age':21,'city':'satara'}
key=input("enter a search key:")
if(d.get(key)!=None ):
    print("key already exist")
else:
    print("key does not in dictionary")