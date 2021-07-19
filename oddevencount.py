elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
sum=0
count=0
while i<len(elements):
    print(elements[i])
    sum=sum+elements[i]
    count=count+1
    i=i+1
print("count",count)
print("sum",sum)
avg=sum/11
print("avg:-",avg)



