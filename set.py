number=[50, 40,  23, 70, 56, 12, 5, 10, 7]
i=0
counter=0
while i< len(number):
    b=(number[i])
    if b>20 and b<40:
        counter=counter+1
        print(b)
    i=i+1
print(counter)


