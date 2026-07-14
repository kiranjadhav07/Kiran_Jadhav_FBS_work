# Q1. Calculate Percentage of Student

# Take input for 5 subjects
sub1 = int(input("Enter Subject 1 Marks: "))
sub2 = int(input("Enter Subject 2 Marks: "))
sub3 = int(input("Enter Subject 3 Marks: "))
sub4 = int(input("Enter Subject 4 Marks: "))
sub5 = int(input("Enter Subject 5 Marks: "))

# Calculate total and percentage
total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = total / 5

# Display result
print(f"Total Marks : {total}")
print(f"Percentage : {percentage}")