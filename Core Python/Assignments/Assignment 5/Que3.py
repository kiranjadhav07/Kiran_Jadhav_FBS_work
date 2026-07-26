#Que3... Accept no. of passengers from user and per ticket cost. Then accept age of each
# passenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

n=int(input("enter  number of passengers:"))
i=1
Total_Ticket=0
while(i<=n):
    Age=int(input("enter the age of {i} person:"))
    ticket=float(input(f"Enter the ticket of {i} person :"))
    if (Age<12):
        Total_Ticket=Total_Ticket+(ticket-ticket *0.3)
    elif(Age>59):
        Total_Ticket=Total_Ticket+(ticket-ticket*0.5)
    else:
        Total_Ticket=Total_Ticket+ticket
    i=i+1
print(f"Total Amount of ticket to travel is {Total_Ticket}")