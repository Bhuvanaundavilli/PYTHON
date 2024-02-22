#write a python program to print average of the matrix
r,c=int(input("rows:")),int(input("columns:"))
l,sum=[],0
for i in range(r):
    l.append(tuple(map(int,input().split())))
for i in l:
    for j in i:
     sum+=j
print(sum/(r*c))
