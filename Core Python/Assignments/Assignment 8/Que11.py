def chkArmstrong(num):
    temp = num
    count = len(str(num))
    sum = 0

    while (num > 0):
        d = num % 10
        sum = sum + (d ** count)
        num = num // 10

    if (temp == sum):
        print(f"{temp} is Armstrong Number")
    else:
        print(f"{temp} is not Armstrong Number")

num = int(input("Enter Number:"))
chkArmstrong(num)