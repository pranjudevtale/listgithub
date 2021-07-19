e = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
i=0
c=0
c1=0

while i<len(e):
    if e[i]%2==0:
        print(e[i],"even number")
        c=c+1
    else:
        print(e[i],"odd number")
        c1=c1+1
    i=i+1
print(c,"even")
print(c1,"odd")

