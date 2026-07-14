# Q5. Calculate Compound Interest



# Take input
p = int(input("Enter Principal: "))
r = int(input("Enter Rate: "))
t = int(input("Enter Time: "))

# Calculate amount and CI
amount = p * (1 + r / 100) ** t
ci = amount - p

# Display result
print("Compound Interest :", ci)
print("Total Amount=",amount)