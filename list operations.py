a=[2,3,4,1,6,7,8,0]
n=len(a)//2
l=[]
for  i in range(n):
	l.extend([a[i],a[i+n]])
print(l)