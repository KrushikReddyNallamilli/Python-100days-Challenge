a=list(map(int,input().split()))
count=0
for i in range(0,len(a)):
	for j in range(a[i],len(a)):
		if a[i]<=a[j]:
			count+=1
print(count)



