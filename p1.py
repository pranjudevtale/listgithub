a=[2,3,"43",5,6,"45",7,"A1","11"]
b=[]
i=0
while i<len(a):
    if type (a[i])==str:
        b.append(a[i])
    i=i+1
print(b)


# for i in a:
#     if type(i)==str:
#         print(i)
