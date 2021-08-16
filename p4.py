a=[4,5,[2,3],4,5,[7],]
b=[]
i=0
sum=0
while i<len(a):
    b.append(a)
    sum=sum+i
    i=i+1
print(sum)



a=[4,5,[2, 3],]
i=0
sum=0
while i<len(a):
    if i<2:
        sum=sum+a[i]
    else:
        j=0
        while j<len(a[i]):
            sum=sum+a[i][j]
            j=j+1
    i=i+1
print(sum)