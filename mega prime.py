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
if (prime(n)==1):
	print("Prime")
	while n:
		r=n%10
		n//=10
		if (prime(r)==1):
			cnt+=1
else:
	print("not prine")
if cnt==len(str(a)):
	print("mega prime")
else:
	print("Not mega prime")


# Mega prime number is a prime number in which all individual digits of the prime number are also prime
# for eg 53 is a prime number
# here both 5 and 3 are also prime so 53 is a Mege Prime Number