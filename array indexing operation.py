# l=list(map(int,input().split()))
# n=int(input())
# if n in l:
# 	for i in l:
# 		if l[i]==n:
# 			print(l[i])
# else:
# 	if l[i]>n:




# arr=list(map(int,input().split()))
# k=int(input())
# sor=sorted(arr)
# if k in arr:
#     print(arr.index(k))
# if k not in arr:
#     for i in range(len(sor)):
#         if k<sor[i]:
#             print(i)
#             break


# arr=list(map(int,input().split()))
# k=int(input())
# if k in arr:
# 	print(arr.index(k))
# else:
# 	arr.append(k)
# 	arr.sort()
# 	print(arr.index(k))

heap,num,itr = list(map(int,input().split())), int(input()),0
while heap[itr] < num:
	itr += 1
print(itr)