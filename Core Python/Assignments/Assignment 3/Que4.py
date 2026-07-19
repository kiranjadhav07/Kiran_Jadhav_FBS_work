#Que4...Write a program to input all sides of a triangle and check wheather triangle is valid or not 


FS=int(input("Enter a first side of:"))
SS=int(input("Enter a Secod side of :"))
TS=int(input("Enter a Third side of:"))
if((FS+SS>TS)and(FS+TS>SS)and(SS+TS>FS)):
    print('Triangle is Valid')
else:
    ('Triangle is not valid')
