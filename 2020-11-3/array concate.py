arr=list(map(int,input().split()))
n=int(input())
l=[]
for i in range(0,n):
	l.append(arr[i])
	l.append(arr[i+n])		
print(l)