def  sum_digits(n):
	s=0
	while n>0:
		rem=n%10
		s=s+rem
		n=n//10
	return s