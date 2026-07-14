# Q7. Find Roots of Quadratic Equation



# Take input
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

# Calculate roots
d = (b * b) - (4 * a * c)

root1 = (-b + d**0.5) / (2 * a)
root2 = (-b - d**0.5) / (2 * a)

# Display result
print("Root1 :", root1)
print("Root2 :", root2)