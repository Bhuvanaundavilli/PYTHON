#write a python program to print the reverse of a number using while loop
n=int(input("Enter a number"))
reverse=0
while n>0:
    digit=n%10
    reverse=reverse*10+digit
    n//=10
print(reverse)
    
