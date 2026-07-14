# Q10. Reverse Three Digit Number

# Take input
num = int(input("Enter three digit number: "))

# Find digits
a = num // 100
b = (num // 10) % 10
c = num % 10

# Reverse number
reverse = (c * 100) + (b * 10) + a

# Display result
print("Reverse Number :", reverse)