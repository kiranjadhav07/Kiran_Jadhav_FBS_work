#Que3...Write a Program to input angles of a triangle and check wheather triangle is valid or not


FA=int(input("Enter a First angle of triangle:"))
SA=int(input("Enter a Second angle of triangle:"))
TA=int(input("Enter a Third angle of triangle:"))
if(FA+SA+TA==180):
    print("Traingle is Valid")
else:
    print("Triangle is non Valid")