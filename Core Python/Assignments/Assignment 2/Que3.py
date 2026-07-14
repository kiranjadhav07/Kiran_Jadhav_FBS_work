# Q3. Convert Feet and Inches into Meter and Centimeter

# Take input
feet = int(input("Enter feet: "))
inch = int(input("Enter inch: "))

# Calculate
total_inch = (feet * 12) + inch
centimeter = total_inch * 2.54
meter = centimeter / 100

# Display result
print("Meter :", meter)
print("Centimeter :", centimeter)