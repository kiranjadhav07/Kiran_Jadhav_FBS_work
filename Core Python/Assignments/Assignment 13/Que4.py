# Que4....python program to generate a dictionary that contains numbers(betwwen 1 and n ) in the form (x,x*x)

# [Without Method]
# n=int(input("enter n:"))
# d={}
# for i in range(1,n+1):
#     d[i]=i*i
# print("Dictionary=",d)

# [With Method]
n=int(input("enter n:"))
d={}
for i in range(1,n+1):
    d.update ({i:i*i})
print("Dictionary=",d)