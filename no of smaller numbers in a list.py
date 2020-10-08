a=[8,1,2,2,3]
s=[]
for i in range(0,len(a)):
	count=0
	for j in range(len(a)):
		if a[j]<a[i]:
			count+=1
	s.append(count)
print(s)


# l=[8,1,2,2,3]
# l2=list()
# for i in range(0,len(l)):
#     c=0
#     for j in range(len(l)):
#         if l[j]<l[i]:
#             c+=1
#     l2.append(c)       
# print(l)
# print(l2)