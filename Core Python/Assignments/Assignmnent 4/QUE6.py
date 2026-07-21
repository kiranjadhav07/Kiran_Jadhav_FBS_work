#QUE6....WAP to check given number is prime or not

# n=int(input("Enter a number:"))
# if n>1:
#     for i in range(2,n):
#         if(n%i==0):
#             print("Number is  not prime")
#             break
#     else:
#         print("Number is  prime")
# else:
#     print("Number is neither prime or nor composite")

n=int(input("Enter a number:"))
for i in range(1, n + 1):
    if (i % 2 !=0 and i % 3 !=0) :
        print(i)
