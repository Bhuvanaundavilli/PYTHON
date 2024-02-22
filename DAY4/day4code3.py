#write a python program to print product of a matrix
'''r,c=int(input("rows:")),int(input("columns:"))
l=[]
for i in range(r):
    l.append(list(map(int,input().split())))
#print(l)
product=1
for r in l:
    print(r)
    for element in r:
        product*=element
print(product)'''

r,c=int(input("rows:")),int(input("columns:"))
l=[]
for i in range(r):
    l.append(list(map(int,input().split())))
#print(l)
product=1
for i in l:
    print(i)
    for j in i:
        product*=j
print(product)
