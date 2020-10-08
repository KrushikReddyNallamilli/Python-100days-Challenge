# # candies=[2,3,5,1,3]

# a=[2,3,5,1,3]
# excan=3
# s=[]
# for i in range(0,len(a)):
# 	if a[i]+excan>=max(a):
# 		s.append("true,")
# 	else:
# 		s.append("false")
# print(s)


a=[2,3,5,1,3]
x=3
m=max(a)
l=[True if i+x>=m else False for i in a]
print(l)