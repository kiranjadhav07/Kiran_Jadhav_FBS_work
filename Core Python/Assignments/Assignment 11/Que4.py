# Que4...python program  to find the second largest number in a list using Bubble sort.

li = [13, 22, 9, 57, 1, 56, 8]
for i in range(1,len(li)):
    for j in range(0, len(li) - i):
        if li[j] > li[j + 1]:
            li[j],li[j+1] = li[j+1],li[j]
print("Sorted list:", li)
print("Second largest number:", li[-2])