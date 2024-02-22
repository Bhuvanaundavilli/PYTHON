#write a python program to remove duplicates in a list
l=list(map(int,input().split()))
l1=[]
for i in l:
    if l not in l1:
       l1.append(i)
print(l1)
