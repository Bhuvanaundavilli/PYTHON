#write a python program to check the given number is strong number or not
def strong(n):
    x,sum=n,0
    while n>0:
        digit=n%10
        fact=1
        for i in range(1,digit+1):
            fact*=i
        sum+=fact
        n//=10
    if sum==x:
        return "strong number"
    else:
        return"not a string number"
n=int(input())
print(strong(n))
