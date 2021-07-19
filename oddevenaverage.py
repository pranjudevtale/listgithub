elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
a=0
b=0
while i<len(elements):
    if elements[i]%2==0:
        print(elements[i],"even")
        a=a+elements[i]
    else:
        print(elements[i],"odd")
        b=b+elements[i]
    i=i+1
print("even",a)
avg=a/4
print(avg)
print("odd",b)
avg=b/7
print(avg)




    
