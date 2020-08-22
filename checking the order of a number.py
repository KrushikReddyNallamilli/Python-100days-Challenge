# def a(n):
# 	rem=0
# 	while n>0:
# 		rem=n%10
# 		n=n//10
# 		return rem
# n=int(input("Enter a number"))
# l=[]
# l.append(rem)
# print(l)

n=input("Enter a number")
asc=n[0]<=n[1]
dsc=n[0]>=n[1]
i=1
while i<(len(n)-1):
	if asc:
		asc=n[i]<=n[i+1]
	elif dsc:
		dsc=n[i]>=n[i+1]
	else:
		break
	i+=1
if asc:
	print("Ascending")
elif dsc:
	print("Descending")
else:
	print("No order")