# def fib(n):
# 	a=0
# 	b=1
# 	sum=1
# 	print(a,b,end=" ")
# 	i=2
# 	while i<n:
# 		c=a+b
# 		sum+=c
# 		print(c,end=" ")
# 		a=b
# 		b=c
# 		i+=1
# 	print("last element:",c)
# 	print("sum=",sum)	
# n=int(input("Enter a number"))
# fib(n)

def fib(n):
	a=0
	b=1
	sum=1
	print(a,b,end=" ")
	i=2
	while i<n:
		c=a+b
		sum+=c
		print(c,end=" ")
		a=b
		b=c
		i+=1
	else:
		print("\nlast element:",c)
		print("sum=",sum)	
n=int(input("Enter a number"))
fib(n)