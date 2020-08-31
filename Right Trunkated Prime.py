# Right trunkated prime
# 239 prime
# 23  prime
# 2   prime

import math
def prime(n):
	for i in range (2,abs(int(math.sqrt(n)))+1):
		if(n%i==0):
			break
	else :
		return(1)


n=int(input("Enter a number"))
a=n
cnt=0
while prime(n) and n>0:
	n=n//10
	if prime(n):
		cnt=1
	else:
		cnt=0
if cnt==1:
	print(a," Right Rrunkated prime")
else:
	print( a," is not a Right Trunkated prime")
	
