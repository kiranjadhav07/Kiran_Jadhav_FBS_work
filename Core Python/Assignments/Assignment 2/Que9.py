# Q9. Swap Two Numbers Without Third Variable

# Take input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Swap numbers
a = a + b
b = a - b
a = a - b

# Display result
print("a :", a)
print("b :", b)