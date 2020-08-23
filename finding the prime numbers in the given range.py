import math
n,n1=map(int,input("Enter a range to check:").split())
if n>n1:
	for k in range(n,n1-1,-1):
		for i in range (2,abs(int(math.sqrt(k)))+1):
			if(k%i==0):
				# print(k,"is not prime")
				break
		else :
			print(k,"is a prime")
	print()
else:
	for k in range(n,n1):
		for i in range (2,abs(int(math.sqrt(k)))+1):
			if(k%i==0):
				# print(k,"is not prime")
				break
		else :
			print(k,"is a prime")