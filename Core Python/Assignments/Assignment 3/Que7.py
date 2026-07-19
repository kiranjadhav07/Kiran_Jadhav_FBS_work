#Que7...WAP tp check if user has entered correct userid and password

Userid=(input("Enter a UserId:"))
password=(input("Enter a password:"))
if(Userid=="Admin" and password=="1234"):
    print("Login Successfully")
else:
    print("Invalid User id or password" )