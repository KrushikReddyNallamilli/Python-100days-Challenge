n=int(input())
def Abundantnum(n):
	s1=0
	for i in range(1,int((n**0.5))+1):
		if n%i==0:
			if i==n//i:
				s1+=i
				
			else:
				s1+=(i+n//i)
	return(s1-n)
def prgm(n):
	if ((Abundantnum(n)>(n))):
		return "Abundant Number"
	else:
	    return "Not Abundant Number"
print(prgm(n))