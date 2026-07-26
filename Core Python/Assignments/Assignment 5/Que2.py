#Que2...Enter number of students from user. For those many students accept marks of 5
# subject marks from user and calculate percentage. Display all percentage and average percentage of students.


n=int(input("enter a number of  students:"))
total_per=0
for i in range(1,n+1):
    print("student",i)
    total=0
    for j in range(1,6):
        marks=int(input(f"enter Marks of subject{j}:"))
        total=total+marks
    per=total/5
    print("percentage=",per)
    total_per=total_per+per
average=total_per/n
print("Average percenatge=",average)
