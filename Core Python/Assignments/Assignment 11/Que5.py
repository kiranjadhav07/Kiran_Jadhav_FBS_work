# Que5...python program to sort a list according to the length of elemnts  within the list..


li = ["swara", "panu", "Ishuuu", "sai", "om"]
print("Original list=",li)
for i in range(1,len(li)):
    for j in range(0,len(li)-i):
        if (len (li[j]) > len(li[j + 1])):
                    li[j],li[j+1] = li[j+1],li[j]
print("Sorted List =", li)