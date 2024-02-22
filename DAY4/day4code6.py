#write a program to print the sum of element in the last column
r,c=int(input("rows:")),int(input("columns:"))
l,sum=[],0
for i in range(r):
    l.append(tuple(map(int,input().split())))
for i in l:
     sum+=i[c-1]
print(sum)
