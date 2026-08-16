# Que6...Python program to multiply all the items in a dictionary.


# [Without Method]
# d={'a':1, 'b': 4, 'c':6,'d':8}
# mul=1
# for i in d:
#     mul=mul*d[i]
# print("Dictionary=",d)
# print("Multiplication of all items=",mul)


# [With Method]
d={'a':1, 'b': 4, 'c':6,'d':8}
mul=1
for i in d.values():
    mul=mul*i
print("Dictionary=",d)
print("Multiplication of all items=",mul)