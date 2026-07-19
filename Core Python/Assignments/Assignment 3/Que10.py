#Que10...WAP to check if person is eligible t0 marry or not

gender=input("Enter the Geder(Male,Female):")
age=int(input("Enter a age:"))
if(gender=='female'):
    if(age>=18):
        print("Eligible for marriage")
    else:
        print("Not eligible for marriage")
else:
    if(age>=21):
        print("Eligible for marriage")
    else:
        print("Not eligible for marriage")