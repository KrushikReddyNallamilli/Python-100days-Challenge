arr=[4,3,12,1,1,1,10,6]
target=[0]*len(arr)
stack=[]
target[-1]=-1
stack.append(arr[-1])
for i in range(len(arr)-2,-1,-1):
	while stack!=[] and arr[i]>=stack[-1]:
		stack.pop()
	if stack==[]:
		target[i]=-1
	else:
		target[i]=stack[-1]
	stack.append(arr[i])
print(target)
