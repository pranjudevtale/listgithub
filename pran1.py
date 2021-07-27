
list1=[1, 2, 3, 4, 5]
list2=[2,3,1,0,5]

i=0
while i<len(list1):
    if list1[i] not in list2:
        print(list1[i])
    i=i+1