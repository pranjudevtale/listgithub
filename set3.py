number=[50, 40, 23, 70, 56, 12, 5, 10, 7] 
i=0
while i<len(number):
    l=number[i]
    if l>number[0] and l<number[3]:
        print("second max",l) 
    i=i+1    

# i=1
# while i<=100:
#     if i%2!=0:
#         print(i,"it is prime number")  
#     elif i==2:
#         print(i,"it is also prime")  
#     else:
#         print(i,"it is not prime") 
#     i=i+1


# import simplejson
# a={1:2}
# f=open("p.json","w")
# p=json.dump(f)
# print(p)


