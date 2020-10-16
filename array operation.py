# l=list(map(int,input().split()))
# c=len(l)
# class Breakit(Exception): pass
# try:
# 	for i in range(len(l)):
# 		if a[i]*2>=max(l):
# 			count+=1
# 		else:
# 			raise Breakit
# 	if count==c:
# 		print("true");
# 	else:
# 		print()
# except Breakit:
#     pass



# def Largest(l):
# 	m=max(l)
# 	for i in l:
# 			if not(i*2<=m) and i!=m:
# 					return -1
# 			else:
# 					return l.index(m)
# l=list(map(int,input().split()))
# print(Largest(l))

# def twice_larg(l):
# 	p=0
# 	l1=[]
# 	l1=sorted(l)
# 	for i in range(len(l1)-1):
# 		if max(l)>=l1[i]*2:
# 			p=l.index(max(l))
# 		else:
# 				p=-1
# 				break
# 	return(p)
# l=list(map(int,input().split()))
# print(twice_larg(l))

a=[3,6,1,0]
m=max(a)
b=a.copy()
b.pop(a.index(m))
c=0
for i in b:
	if m>=2*i:
		c+=1
if c==len(b):
	print(a.index(m))
else:
	print(-1)