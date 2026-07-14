# Q1. Convert Time into Seconds

# Take input
hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))

# Calculate total seconds
total_seconds = (hours * 3600) + (minutes * 60) + seconds

# Display result
print("Total Seconds :", total_seconds)