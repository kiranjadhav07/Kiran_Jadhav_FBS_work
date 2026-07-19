#Que9...Input 5 subject marks from user and display grade

s1=int(input("Enter a marks of subject 1:"))
s2=int(input("Enter a marks of subject 2:"))
s3=int(input("Enter a marks of subject 3:"))
s4=int(input("Enter a marks of subject 4:"))
s5=int(input("Enter a marks of subject 5:"))
total=s1+s2+s3+s4+s5
percentage=total/500*100
if("percentage>=70"):
    print("First Class")
elif("percentage>=50"):
    print("Second Class")
elif("percentage>=40"):
    print("Third class")
elif("percentage>=35"):
    print("pass class")
else:
    print("fail")