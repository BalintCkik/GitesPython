t=[2, 0, 4, 1, 15, 11, 22, 14, 16, 2, 0, 31]
n=len(t)
print(t)
poz=0
neg=0

for i in range(0,n-1):
    for j in range(i+1,n):
        if(t[i]<t[j]):
            poz+=1
        if(t[i]>t[j]):
            neg+=1
if(poz>neg):
    print("Igaz, hogy mindig több szállt fel, mint le!")
if(poz<neg):
    print("Nem igaz, hogy mindig több szállt fel, mint le!")

tb=[2, 0, 4, 1, 15, 11, 100, 14, 16, 2, 0, 109]
max=tb[0]
for i in range(n):
    if(tb[i]>max):
        max=tb[i]
print(i,". megállóban voltak a legtöbben!")