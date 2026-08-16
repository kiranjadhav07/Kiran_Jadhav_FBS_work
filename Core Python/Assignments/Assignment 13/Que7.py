# Que7...Python program to remove the given key from a dictionary.
d={'id':101,'name':'kiran','age':21,'city':'satara'}
key=input("Enter key to remove:")
if key in d:
    d.pop(key)
    print("updated dictionary=",d)
else:
    print("key does not exist")