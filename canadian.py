# Canadian or canada number
# if sum of the factors square other than 1 and itself is equal to sum individual digits square of a given number 
# 125 
# 581
# 16999


# n=int(input())
# num=n
# sum1=0
# sum2=0
# while(num>0):
#     nu=num%10
#     sum1+=nu**2
#     num//=10
# for i in range(2,n//2):
#     if(n%i==0):
#         sum2+=i
# if(sum1==sum2):
#     print("yes")
# else:
#     print("no")

# def boring(n):
# 	s = [i for i in range(1,n+1) if n%i == 0]
# 	r = 0
# 	while n>0:
# 		r += (n%10)**2
# 		n//=10
# 	return r == sum(s[1:-1])
	
# print(boring(int(input())))

# n=int(input())
# def num(n):
# 	s=0
# 	while (n>0):
# 		r=n%10
# 		s=s+r**2
# 		n=n//10
# 	return(s)
# def xyz(n):
# 	s1=0
# 	for i in range (2,n//2+1):
# 		if n%i==0:
# 			print(i)
# 			s1+=i	
# 	if (s1)==num(n):
# 		return "true"
# 	else:
# 		return "False"
# print(xyz(n))


# n=int(input())
# def num(n):
# 	s=0
# 	while (n>0):
# 		r=n%10
# 		s=s+r**2
# 		n=n//10
# 	return(s)
# def xyz(n):
# 	s1=0
# 	for i in range(1,int((n**0.5))+1):
# 		if n%i==0:
# 			if i==n//i:
# 				s1+=i
				
# 			else:
# 				s1+=(i+n//i)
# 	return(s1-1-n)
# def prgm(n):
# 	return (xyz(n)==num(n))
# if prgm(n):
# 	print('yes')
# else:
# 	print('no')






n=int(input())
def num(n):
	s=0
	while (n>0):
		r=n%10
		s=s+r**2
		n=n//10
	return(s)
def xyz(n):
	s1=0
	for i in range(1,int((n**0.5))+1):
		if n%i==0:
			if i==n//i:
				s1+=i
				
			else:
				s1+=(i+n//i)
	return(s1-1-n)
def prgm(n):
	if ((xyz(n)==num(n))):
		return(True)
	else:
		return(False)
print(prgm(n))