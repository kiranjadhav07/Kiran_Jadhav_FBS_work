# Q11. Find Minimum Number of Notes

# Take input
amount = int(input("Enter amount: "))

# Calculate notes
note500 = amount // 500
amount = amount % 500

note200 = amount // 200
amount = amount % 200

note100 = amount // 100
amount = amount % 100

note50 = amount // 50
amount = amount % 50

note20 = amount // 20
amount = amount % 20

note10 = amount // 10
amount = amount % 10

# Display result
print("500 Notes :", note500)
print("200 Notes :", note200)
print("100 Notes :", note100)
print("50 Notes :", note50)
print("20 Notes :", note20)
print("10 Notes :", note10)