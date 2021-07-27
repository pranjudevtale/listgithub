# name=["s","a","l","o","n","i"]
# l=[]
# i=0
# length=len(name)
# while i<length:
#     a=length-i-1
#     b=name[a]
#     l.append(b)
#     i=i+1
# if l==name:
#     print("it is polindrome name")
# else:
#     print("it is not polindrome name")


# name=["m","a","m"]
# l=[]
# i=0
# length=len(name)
# while i<length:
#     a=length-i-1
#     b=len(name)
#     l.append(b)
#     i=i+1
# if i==name:
#     print("it is polindrome name")
# else:
#     print("it is not polindrome name")


i=int(input("enter the number"))
rev=0
x=i
while i>0:
    rev=(rev*10)+i%10
    i=i//10
if x==rev:
    print("it is palindrome")
else:
    print("it is not palindrome")

# name=input("entewr the name")
# i=len(name)-1
# n=name
# temp=[]
# while i>=0:
#     t=(name[i])
#     temp.append(t)
#     i=i-1
# print(temp)
# if temp==n:
#     print("it is palindrome")
# else:
#     print("it is not palindrome " )
