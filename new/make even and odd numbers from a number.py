num=int(input())
even=0
odd=0
ec=1
oc=1
while num:
	r=num%10
	num=num//10
	if r%2:
		odd=odd+r*oc
		oc=oc*10
	else:
		even=even+r*ec
		ec=ec*10
print(even,odd)