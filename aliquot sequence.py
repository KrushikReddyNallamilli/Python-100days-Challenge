# Aliquot sequence
# 10 factors=5,2,1
# 5+2+1=8
# 8 factors=4,2,1
# 4+2+1=7
# factors=1
# 1 break


def aliquot(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            print(i,end=" ")
            sum=sum+i
    print("sum - ",sum)       
    return sum       
n=int(input())
s=aliquot(n)
if n!=s:
    while s!=1:
        s=aliquot(s)