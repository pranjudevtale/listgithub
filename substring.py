
s = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
l=s.split()
i=0
while i<len(l):
    if l[i]=="over":
        i=i+1
    print(l[i],end="  ")
    i=i+1


# a=[2,3,"43",5,6,"45",7,"A1","11"]
# b=[]
# i=0
# while i<len(a):
#     if a[i]==type(str):
#         b.append(a)
#     i=i+1
# print(b)





