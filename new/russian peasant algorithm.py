
# def alog(a,b):
# 	ans=0
# 	while(a >0):
# 		if a%2:
# 			ans+=b
# 		a=a//2
# 		b=b*2
# 	return(ans)
# a=int(input())
# b=int(input())
# print(alog(a,b))


def mul(a,b):
	if a==1:
		return b
	if a%2:
		return b+mul(a//2,b*2)
	else:
		return mul(a//2,b*2)
a,b=map(int,input().split())
print(mul(a,b))