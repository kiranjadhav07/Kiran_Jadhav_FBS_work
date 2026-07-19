#Que6...WAP to calculate profit or loss

sp=int(input("Enter a selling price:"))
cp=int(input("Enter a cost price:"))
if (sp>cp):
    print("Profit")
elif(sp<cp):
    print("Loss")
else:
    print("No profit","No Loss")