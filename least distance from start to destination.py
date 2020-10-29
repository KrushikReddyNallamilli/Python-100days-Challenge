# a=[1,2,3,4]
# a.append(a[0])
# res=float("inf")
# start=int(input())
# end=int(input())
# num=0
# for i in range(start,end):
#     num+=a[i]
# res=min(res,num)
# print(res)
# num=0
# for i in range(end,start,-1):
#     num+=a[i]
# res=min(res,num)
# print(res)

# l=list(map(int,input().split()))
# s=int(input())
# d=int(input())
# min=0
# max=l[s]
# for i in range(s,d):
#     min=min+l[i]
# for i in range(d,0,-1):
#     max=max+l[i]
# if min:
# 	print(min)
# else:
#     print(max)


def mindist(arr,s,d):
	t=sum(arr)
	d1=sum(arr[s:d])
	d2=t-d1
	print(d1,d2)
	return min(d2,d1)
arr=list(map(int,input().split()))
s=int(input())
d=int(input())
print(mindist(arr,s,d))