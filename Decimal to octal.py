# n=33
# a=''
# while n>0:
#     a+=str(n%8)
#     n=n//8
# print(a[::-1])

n=int(input())
sum1=""
while(n>0):
	rem=n%8
	sum1+=str(rem)
	n=n//8
print(sum1[::-1])

