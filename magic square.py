magic = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
]
i=0
sum=0
while i<len(magic):
    col=0
    while col<len(magic):
        sum=sum+magic[i][col]
        col=col+1
        j=0
        sum1=0
        while j<len(magic):
            row=0
            while row<len(magic):
                sum1=sum1+magic[j][row]
                row=row+1
            j=j+1
            k=0
            sum2=0
            while k<len(magic):
                dig=0
                while dig<len(magic):
                    sum2=sum2+magic[i][dig]
                    dig=dig+1
                k=k+1
        i=i+1
print(sum)
print(sum1)
print(sum2)
if sum==sum1==sum2:
    print("it is magic square")
else:
    print("it is not magic square")

    

    
    


