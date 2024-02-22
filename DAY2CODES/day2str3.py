#write a python program to print count of owels in both even position and odd position
s=input()
for i in range(len(s)):
    if i%2==0:
        if s[i] in "aeiouAEIOU":
            ec+=1
    else:
        if s[i] in "aeiouAEIOU":
            oc+=1
print(ec,oc)
