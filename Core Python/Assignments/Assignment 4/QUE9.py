#QUE9....WAP to  print all numbers in range divisible by a given number

n=int(input("Enter a number:"))
start=int(input("Enter a starting number:"))
end=int(input("Enter a ending number:"))
for i in range(start,end+1):
    if(i%n==0):
        print(i)


