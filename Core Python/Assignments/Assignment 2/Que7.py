# Q7. Find Sum of Three Digit Number

# Take input
num = int(input("Enter three digit number: "))

# Find digits
a = num // 100
b = (num // 10) % 10
c = num % 10

# Calculate sum
sum = a + b + c

# Display result
print("Sum :", sum)