# Q8. Convert Days into Years, Weeks and Days

# Take input
days = int(input("Enter days: "))

# Convert
years = days // 365
days = days % 365

weeks = days // 7
days = days % 7

# Display result
print("Years :", years)
print("Weeks :", weeks)
print("Days :", days)