# Que2....write a program to calculate simple interest based on principle,rate, time.

p = int(input("Enter Principal: "))
r = int(input("Enter Rate: "))
t = int(input("Enter Time: "))
si = p * r * t / 100
print("Simple Interest =", si)