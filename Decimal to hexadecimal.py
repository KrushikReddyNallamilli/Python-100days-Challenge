# n=2545
# h=''
# while n>0:
#     r=n%16
#     if(r<10):
#     	h+=str(chr(r+48)) #Ascii value 0f 0 is 48
#     else:
#     	h+=str(chr(r+55))
#     n=n//16
# print(h[::-1])



n=int(input())
res=''
while n>0:
	a=n%16
	if a>=10 and a<=15:
		a=a%10
		res+=chr(65+a)
	else:
		res+=str(a)
	n=n//16
print(res[::-1])