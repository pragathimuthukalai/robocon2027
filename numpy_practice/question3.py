n=int(input("Enter a Number:"))

num=str(n)
sum=0
for i in range(len(num)):
    sum += int(num[i])**(i+1)
if sum==n:
    print(n,"is disarium number")
else:
    print(n,"is not disarium number")

