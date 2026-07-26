#Que1.... Write a program to prompt user to enter userid and password. If Id and password is incorrect give him chance to re-enter the credentials. Let him try 3  times. After that program to terminate.


userid='admin'
password='0728'
attempt=1
while attempt<3:
    uid=input("enter User Id:")
    pasword=input("Enter password:")
    if(uid==userid and pasword==password):
        print("Login successfully")
        break
    else:
        print("Invalid  Userid or password")
        attempt=4
if attempt==4:
    print("program Terminated")