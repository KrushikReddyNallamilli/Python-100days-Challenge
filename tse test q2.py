# suppose you have a long flower bed  in which some of the plots are planted and some are not .However ,flowers cannot be planted in adjacent  okits- they wold compete for water and both die
# given a flowerbed(represent as an array containing 0 & 1, hwere 0 means empty and 1 means not empty ),and a number n,return if n new new flowers can be planted in it without violiting the no-adjacent -flowers rule


# eg1:
# 5
# 1 0 0 0 1
# 1
# output : true



# # n=int(input())
# arr=list(map(int,input().split()))
# n=len(arr)
# flowers=int(input())
# c=0
# for i in arr:
#     if i==1:
#         c+=1
# if n%2!=0 and c+flowers<=n//2+1:
#     print(True)
# elif n%2==0 and c+flowers<=n//2:
#     print(True)
# else:
#     print(False)



# n=int(input())
# l=list(map(int, input (). split ()))
# d=int(input())
# for j in range(len(l)):
# 	if l[j]==1:
# 		for k in range(l.index(1)+1,(d*2)+2):
# 			if l[k]==1:
# 				c=1
# 				break
# 		else:
# 			c=0
# if c==0:
# 	print (True)
# else:
# 	print (False)



def fun(fb,n):
	fb=[0]+fb+[0]
	c=0
	for i in range(len(fb)):
		if fb[i:i+3]==[0,0,0]:
			c+=1
			if c>=n:
				return True
			fb[i+1]=1
	return c>=n
fb=[0,0,0,0,0,0,0]
n=