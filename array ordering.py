# arr1=list(map(int,input().split()))
# arr2=list(map(int,input().split()))
# l=[]
# for i in range(len(arr2)):
# 	for j in range(len(arr1)):
# 		if arr2[i]==arr1[j]:
# 			l.append(arr1[j])
# 			del arr1[j]

# def SortArray(arr1,arr2):
# 	c = 0
# 	final = []
# 	for i in arr2:
# 		c = arr1.count(i)
# 		print(c)
# 		for j in range(c):
# 			final.append(i)
# 			arr1.remove(i)
# 			arr1.sort()
# 			final.extend(arr1)
# 			print(final)
# 			return final
# arr1=[2,3,1,3,2,4,6,7,9,2,19]
# arr2=[2,1,4,3,9,6]
# SortArray(arr1,arr2)




a=[2,3,1,3,2,4,6,7,9,2,19]
b=[2,1,4,3,9,6]
l=[]
for i in b:
    l.extend([i]*a.count(i))
c=set(a)-set(b)
c=list(c)
c.sort()
# for i in c:
# 	l.extend([c]*a.count(c))
l.extend(c)	
print(l)