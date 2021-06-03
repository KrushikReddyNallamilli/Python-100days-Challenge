def gen_fib(num,a=0,b=1):
	n=num
	while(num):
		if n==num:
			print(a,end=" ")
		elif n-1==num:
			print(b,end=" ")
		else:
			c=a+b
			a=b
			b=c
			print(c,end=" ")
		num-=1
num=int(input())
gen_fib(num)
