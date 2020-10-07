# a=[2,3,5,6]
# b=[7,6]
# # a=list(set(a)|set(b))
# # print(a)



# # for i in b:
# # 	if i in a:
# # 		pass
# # 	else:
# # 		a.append(i)
# # print(a)



# for i in b:
# 	if i not in a:
# 		a.append(i)
# print(a)

# #################################################################################

# input:[2,0,5,0,4,5]
# output:[2,5,4,0,0]

# l=[2,0,5,0,4,5]
# for i in range(0,len(l)):
# 	if l[i]==0:
# 		l.pop(i)
# 		l.append(0)
# print(l)


# l=[2,0,5,0,4,5]
# c=0
# for i in range(len(l)):
# 	if l[i]!=0:
# 		m=l[i]
# 		l[i]=l[c]
# 		l[c]=m
# 		c+=1
# print(l)
# wava form of numbers
# input=[2 5 3 4 6]
# output = True
# input=[2 5 6 3 4]
# output= false 


###################################################################################
a=[i for i in range(5) if i!=2]
print(a)