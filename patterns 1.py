 #     *
 #    **
 #   ***
 #  ****
 # *****
 #  ****
 #   ***
 #    **
 #     *


# n=int(input())
# for i in range(1,n+1):
# 	print(" "*(n-i),"*"*i)
# for i in range(n-1,0,-1):
# 	print(" "*(n-i),"*"*i)

n=int(input()) #3
for i in range(n,-(n+1),-1): #3,2,1,0,-1,-2,-3
	for j in range(abs(i),0,-1):
		 print(" ",end="")
	for k in range(abs(i),n+1):
		print("*",end="")
	print()	