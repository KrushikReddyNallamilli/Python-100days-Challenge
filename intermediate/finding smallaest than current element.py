arr=[2,3,1,2,4,2]
target=[0]*len(arr)
stack=[]
target[-1]=arr[-1]
stack.append(arr[-1])
s=0
s+=arr[-1]
for i in range(len(arr)-2,-1,-1):
	while stack!=[] and arr[i]<stack[-1]:
		stack.pop()
	if stack==[]:
		target[i]= arr[i]
	else:
		target[i]=arr[i]-stack[-1]
	s+=target[i]
	stack.append(arr[i])
print(target,"=>",s)