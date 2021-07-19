list1=[1, 2, 3, 4, 5, 6]
list2=[2, 3, 1, 0, 6, 7]
i=0
k=[]
while i<len(list1):
    s=list1[i]
    if s not in list2:
        k.append(s)
    i=i+1
print(k)