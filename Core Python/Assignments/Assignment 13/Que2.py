# Que2...python program to concatentae two dictionaries into one.

# [Without Method]
# d1={'a':10,'b':20}
# d2={'c':30,'d':40}
# d={}
# for key in d1:
#     d[key]=d1[key]
# for key in d2:
#     d[key]=d2[key]
# print("Dictionary1=",d1)
# print("Dictionary2=",d2)
# print("concatented=",d)

# [With Method]
d1={'a':10,'b':20}
d2={'c':30,'d':40}
print("Dictionary1=",d1)
d1.update(d2)
print("Dictionary2=",d2)
print("concatented=",d1)