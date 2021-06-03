num1=12
num2=24
r=2
res=1
while True:
	if(num1%r==0 and num2%r==0):
		num1=num1//r
		num2=num2//r
		res=res*r
	else:
		r+=1
	if(r>num1 or r>num2) :
		break
print(res*num1*num2)
