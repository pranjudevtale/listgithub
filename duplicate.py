

n=[19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11] 
i=0
a=[]
while i<len(n):
    l=n[i]
    if l not in a:
        a.append(l)
    i=i+1
print(a)



# a=[3, 2, 6,  9, 8, 7]
# i=0
# while i<len(a):
#     j=i+1
#     while j<len(a):
#         if a[i]>a[j]:
#             c=[i]
#             a[i]=a[j]
#             a[j]=c
#         j=j+1
#     i=i+1
# print(a)