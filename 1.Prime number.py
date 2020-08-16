#prime number

# count=0
# n=int(input("Enter a number"))
# for i in range (1,n+1):
# 	if(n%i==0):
# 		count+=1;
# if count==2:
# 	print(n,"is prime")
# else :
# 	print(n,"is not a prime")

# count=0
# n=int(input("Enter a number"))
# for i in range (2,n):
# 	if(n%i==0):
# 		count+=1;
# if count>0:
# 	print(n,"is not prime")
# else :
# 	print(n,"is a prime")

# count=0
# n=int(input("Enter a number"))
# if n>1:
# 	for i in range (2,n):
# 		if(n%i==0):
# 			print(n,"is not prime")
# 			break
# 	else :
# 		print(n,"is a prime")
# else:
# 	print("enter number greater than 1")

# count=0
# n=int(input("Enter a number"))
# for i in range (2,n//2+1):
# 	if(n%i==0):
# 		count+=1;
# if count>0:
# 	print(n,"is not prime")
# else :
# 	print(n,"is a prime")

# import math
# n=int(input("Enter a number"))
# for i in range (2,abs(int(math.sqrt(n)))+1):
# 	if(n%i==0):
# 		print(n,"is not prime")
# 		break
# else :
# 	print(n,"is a prime")

import math
n=int(input("Enter a number"))
i=2
while i<=abs(int(math.sqrt(n))):
	if(n%i==0):
		print(n,"is not prime")
		break
	i+=1
else :
	print(n,"is a prime")

