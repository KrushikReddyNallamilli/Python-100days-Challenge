a=[2,3,1,5,4]
status=True
for i in range (len(a)-1):
	if a[i]<a[i+1] and i%2==0:
		status=True
	elif a[i]>a[i+1] and i%2==1:
		status=True
	else:
		status=False
		break
print(status)
