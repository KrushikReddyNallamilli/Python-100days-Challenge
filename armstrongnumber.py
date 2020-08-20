def  armstrong(n):
	k=n
	s=0
	while n>0:
		rem=n%10
		s=s+(rem*rem*rem)
		n=n//10
	if(k==s):
		return('Armstrong')
	else:
		return("Not Armstrong")
n=int(input("Enter a number: "))
print(armstrong(n))



