num=int(input("enter a number"))
i=1
a=["q","z"]
k=[]
while i<=num :
        j=0
        while j<len(a):
                n=a[j]
                m=str(n+str(i))
                k.append(m)
                j=j+1
        i=i+1
print(k)