def length(n):
	count=0
	while (n>0):
		count+=1
		n=n//10
	return count

def  armstrong(n):
	k=n
	s=0
	l=length(n)
	while n>0:
		rem=n%10
		s=s+(rem**l)
		n=n//10
	if(k==s):
		return('Armstrong')
	else:
		return("Not Armstrong")
n=int(input("Enter a number: "))
print(armstrong(n))



