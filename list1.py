# p=[['p','r','a','n','j','u'],['b','e','s','t']]
# i=0
# a=[]
# while i<len(p):
#     j=0
#     while j<len(p[i]):
#         print(p[i],end="")
#         a.append(p)
#         j=j+1
#     i=i+1
# # print()

# a="pranju"
# i=0
# while i<len(a):
#     j=0
#     while j<=i:
#         print(a[j],end=" ")
#         j=j+1
#     print()
#     i=i+1

# a=[1,2, 3, 4, 5]
# i=0
# while i<len(a):
#     b=a[i]*a[i]
#     print(b)
#     i=i+1

# a=[[2,3],[4,5],[2,3]]
# i=0
# while i<len(a):
#     b=a[i][i]*a[i][i]*a[i][i]#*a[i][i]
#     print(b)
#     i=i+1

list=[0,1,-4,-5,6,7,-8,9]
a=[]
i=0
while i<len(list):
    if list[i]<0:
        print(list[-i]*0)
    else:
        print(list[i])
        a.append(list[i])
    i=i+1

a=[2,3,"43",5,6,"45",7,"A1","11"]
b=[]
i=0
while i<len(a):
    if type (a[i])==str:
        b.append(a[i])
    i=i+1
print(b)

