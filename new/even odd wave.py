def is_even_odd_wave(num):
	d=num%10
	num=num//10
	while(num):
		r=num%10
		num=num//10
		if(r%2==0 and d%2==0) or(r%2 and d%2):
			return False
		else:
			d=r
	return(True)

T=int(input())
for _ in range(T):
	num=int(input())
	print(is_even_odd_wave(num))
