# left trunkated prime
# 179 prime
# 79  prime
# 9   prime


def prime(n):
    for i in range(2,n):
        if(n%i==0):
            break
    else:
        return(1)
n=int(input())
leng=len(str(n))
cnt=0
while(prime(n)==1 and n>0):
    num=10**(leng-1)
    n%=num
    leng-=1
    if(prime(n)==1):
        cnt=1
    else:
        break
if(cnt==1):
    print("yes left truncatable prime")
else:
    print("not left truncatable prime")



# import math
# def prime(n):
#     for i in range (2,abs(int(math.sqrt(n)))+1):
#         if(n%i==0):
#             break
#     else :
#         return(1)


# n=str(input("Enter a number"))
# n=n[::-1]
# n=int(a)
# a=n
# cnt=0
# while prime(n) and n>0:
#     n=n//10
#     if prime(n):
#         cnt=1
#     else:
#         cnt=0
# if cnt==1:
#     print(a," Left Rrunkated prime")
# else:
#     print( a," is not a Left Trunkated prime")
    
