# Binary	0,1
# decimal	0,1,2,3,4,5,6,7,8,9
# octal	0,1,2,3,4,5,6,7
# hexadecimal	0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F

# n=111
# d=0
# b=1
# while n:
# 	r=n%10
# 	n=n//10
# 	d+=r*b
# 	b*=2
# print(d)


b=input("b:")
dec=0
j=0
for i in range(len(b)-1,-1,-1):
	dec+=int(b[i])*(2**j)
	j+=1
print(dec)