def fun(n,array,ele):
	count=0
	for i in range(n):
		if array[i]==ele:
			count+=1
	print(n-count)
	
n=int(input())
array=list(map(int,input().split()))
ele=int(input())
fun(n,array,ele)