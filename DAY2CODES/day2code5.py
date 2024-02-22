#write a python program to check given number is perfect number or not
n=int(input("Enter a number"))
c=0
for i in range(1,n):
    if n%i==0:
        c+=i
if c==n:
    print("perfect Number")
else:
    print("not a perfect number")
