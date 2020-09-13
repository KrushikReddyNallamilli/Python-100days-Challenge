# #PERFECT number:
# Ex:
# 6
# sum of 6 divisors
# 3+2+1=6
# output: yes

# Eg :28,496

# 10
# sum of 10 divisors
# 5+2+1=8
# output: No


# def perfectnum(n):
# 	c=0
# 	for i in range(1,n//2+1):
# 		if n%i==0:
# 			c+=i
# 	if c==n:
# 		return "perfect num"
# 	else:
# 		return "Not a perfect num"
# n=int(input())
# print(perfectnum(n))


n=int(input())
def perfectnum(n):
	s1=0
	for i in range(1,int((n**0.5))+1):
		if n%i==0:
			if i==n//i:
				s1+=i
				
			else:
				s1+=(i+n//i)
	return(s1-n)
def prgm(n):
	if ((perfectnum(n)==(n))):
		return(True)
	else:
		return(False)
print(prgm(n))