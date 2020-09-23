# Binary	0,1
# decimal	0,1,2,3,4,5,6,7,8,9
# octal	0,1,2,3,4,5,6,7
# hexadecimal	0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F


n=int(input())
d=''
while (n>0):
	d += str(n%2)
	n=n//2
print(d[::-1])

