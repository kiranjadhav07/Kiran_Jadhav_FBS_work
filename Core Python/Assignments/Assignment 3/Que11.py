#Que11...Accept age of five people and also per person ticket amount and then calculate total amount to ticket to travel for all of them based on following condition : a. Children below 12 = 30% discount b. Senior citizen (above 59) = 50% discount c. Others need to pay full.


age = int(input("Enter 1st Person Age: "))
ticket = int(input("Enter 1st Person Ticket Price: "))
total_ticket = 0

if age < 12:
    total_ticket = total_ticket + (ticket - ticket * 0.30)
elif age > 59:
    total_ticket = total_ticket + (ticket - ticket * 0.50)
else:
    total_ticket = total_ticket + ticket


age = int(input("Enter 2nd Person Age: "))
ticket = int(input("Enter 2nd Person Ticket Price: "))

if age < 12:
    total_ticket = total_ticket + (ticket - ticket * 0.30)
elif age > 59:
    total_ticket = total_ticket + (ticket - ticket * 0.50)
else:
    total_ticket = total_ticket + ticket


age = int(input("Enter 3rd Person Age: "))
ticket = int(input("Enter 3rd Person Ticket Price: "))

if age < 12:
    total_ticket = total_ticket + (ticket - ticket * 0.30)
elif age > 59:
    total_ticket = total_ticket + (ticket - ticket * 0.50)
else:
    total_ticket = total_ticket + ticket


age = int(input("Enter 4th Person Age: "))
ticket = int(input("Enter 4th Person Ticket Price: "))

if age < 12:
    total_ticket = total_ticket + (ticket - ticket * 0.30)
elif age > 59:
    total_ticket = total_ticket + (ticket - ticket * 0.50)
else:
    total_ticket = total_ticket + ticket


age = int(input("Enter 5th Person Age: "))
ticket = int(input("Enter 5th Person Ticket Price: "))

if age < 12:
    total_ticket = total_ticket + (ticket - ticket * 0.30)
elif age > 59:
    total_ticket = total_ticket + (ticket - ticket * 0.50)
else:
    total_ticket = total_ticket + ticket

print("Total Ticket Amount =", total_ticket)