# matrix=[[1, 2, 3, ],[4, 5],[6, 7, 8, 9]]
# a=[]
# i=0
# while i<len(matrix):
#     l=matrix[i]
#     a.append(matrix[i])
#     i=i+1
# print(a)

matrix=[[0, 1, 2, 3, 4],
        [0,1, 2, 3, 4],
        [0, 1, 2, 3, 4]
]
a=[]
for i in range(3):
    a.append(matrix[i])
    for j in range (3):
        a[i].append(i)
print(a)


