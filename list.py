a=[1,2,3,5,9,24,56,12,5,6,]
i=0
b=[]
while i<len(a):
    if a[i]%3==0:
        # print(3)
        b.append(3)
    else:
        # print(a[i])
        b.append(a[i])
    i=i+1
print(b)

# d=[1,2,[3,8,9],12,5,3,[6,5,4]]
# i=0
# sum=0
# while i<len(d):
#     if type(d[i])==type(d):
#         j=0
#         while j<len(d[i]):
#             sum=sum+d[i][j]
#             j=j+1
#     else:
#         sum=sum+d[i]
#     i=i+1
# print(sum)


# a=[1,2,1,2,3,4,3,4]
# i=0
# product=1
# sum=0
# while i<len(a):
#     j=i
#     while j<len(a):
#         if a[i]==a[j]:
#             del(a[i])
#             product=product*(a[i])
#             sum=sum+a[i]
#         j=j+1
#     i=i+1
# print(product)
# print(sum)

a=[[1,2,3],[4,5,6],[7,8,9]]
i=0
while i<len(a):
    if type(a[i])==list:
        j=0
        while j<len(a[i]):
            print(a[i][j])
            j=j+1
    i=i+1

# a=[[1,2,3],[4,5,6],[7,8,9]]
# i=0
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         while j<len(a[i]):
#             print(a[i][j])
#             j=j+1
#         i=i+1

# a=[1,2,3,4,5,6]
# i=0
# sum=0
# while i<len(a):
#     sum=sum+a[i]
#     print(a[i]*i)
#     i=i+1
# print(sum)

# a=input("enter the number")
# b=[]
# for i in a:
#     for j in i:
#         b.append(j)
# print(b)

#o/p=['p','r','a','n','j','u']

# a=input("enter the number:-")
# b=[]
# for i in a:
#     for j in i:
#         b.append(j)
# print(b)

# list1=[1, 2, 3, 4, 5]
# list2=[2,3,1,0,5]

# i=0
# while i<len(list1):
#     if list1[i] not in list2:
#         print(list1[i])
#     i=i+1

# a=["one","two","three","four","five"]
# b=[1, 2, 3, 4, 5]
# # p=dict(zip(a,b))
# # print(dict(p))
# p=0
# j={}
# for i in a:
#     j[i]=b[p]
#     p=p+1
# print(j)


# a=[1,2,3,4,5,"p","y","t","h","o","n"]
# i=0
# p=[]
# while i<len(a):
#     if type(a[i])==int:
#         p.append(a[i])
#     i=i+1
# print(p)

# n=input("enter the name:-")
# a=[]
# i=0
# while i<len(n):
#     a.append(n[i])
#     i=i+1
# print(a)
# c=[]
# j=0
# while j<len(a):
#     if a[j]=="a" or a[j]=="e" or a[j]=="i" or a[j]=="o" or a[j]=="u":
#         c.append(a[j])
#     j=j+1

# print(c)

# def num(a):
#     sum=a
#     avg=sum/2
#     print(avg)
# num(int(input("enter the number:-")))

# num=int(input("enter the number:-"))
# a=num%10
# print(a)

# a=[1,2,3,[4,5,6,9,8],5,9]
# a[2]=12
# print(a)



# a=["prnju","ankita","ashu","pri"]
# a.insert(3,"asmita")
# print(a)
