a=list(map(int,input().split()))
l=[]
for i in range (len(a)):
	for j in range(i+1,len(a)):
		if a[j]<a[i]:
			l.append(a[i]-a[j])
			break
	else:
		l.append(a[i])
print(l)


