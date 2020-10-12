# def fun(n,array,ele):
# 	count=0
# 	l=[]
# 	for i in range(n):
# 		if array[i]==ele:
# 			count+=1
# 			l.append(i)
# 	if count==0:
# 		print("-1 -1")
# 	else:
# 		print(l)

# n=int(input())
# array=list(map(int,input().split()))
# ele=int(input())
# fun(n,array,ele)


# def sorted_array(arr,target_value,n):
#     l=[]
#     for i in range(n):
#         if arr[i]==target_value:
#             l.append(i)
#     if l==[]:
#         print("-1 -1")
#     else:
#         print(l[0],l[-1])
# n=int(input())
# arr=list(map(int,input().split()))
# target_value=int(input())
# sorted_array(arr,target_value,n)


def fun(n,array,ele):
	count=0
	l=[]
	for i in range(n):
		if array[i]==ele:
			count+=1
			l.append(i)
	if count==0:
		print("-1 -1")
	else:
		print(l[0],l[-1])

n=int(input())
array=list(map(int,input().split()))
ele=int(input())
fun(n,array,ele)