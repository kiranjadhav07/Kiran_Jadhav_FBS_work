# Q6. Calculate Total Salary

# Take input
basic = int(input("Enter Basic Salary: "))

# Calculate DA, TA and HRA
da = basic * 10 / 100
ta = basic * 12 / 100
hra = basic * 15 / 100

salary = basic + da + ta + hra

# Display result
print("Total Salary :", salary)