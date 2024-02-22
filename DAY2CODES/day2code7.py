#write a python program to show the given number is arm strong or not
n=int(input("Enter a number"))
temp=n
rev=0
while n>0:
    digit=n%10
    rev=rev+digit**3
    n//=10
if rev==temp:
    print("Amstrong")
else:
    print("not amstrong")
