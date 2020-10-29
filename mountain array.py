# def mountain(arr)->bool:
# 	n = len(arr)
# 	if n<3:
# 		return False
# 	i= 0
# 	asc,dsc = 0,0
# 	while i < n-1:
# 		asc = 1
# 		if arr[i]>=arr[i+1]:
# 			break
# 		i += 1
# 	while i < n-1:
# 		dsc= 1
# 		if arr[i] <= arr[i+1]:
# 			break
# 		i += 1
# 	return n == i+1 and asc and dsc
# arr = list(map(int,input().split()))
# print(mountain(arr))



l=[0,2,3,4,5,2,1,0]
if l.index(max(l))==len(l)-1:
    print("False")
else:
    for i in range(0,l.index(max(l))-1):
        if not l[i]<l[i+1]:
            print("False")
            break
    else:
        for i in range(l.index(max(l)),len(l)-1):
            if not l[i]>l[i+1]:
                print("False")
                break
        else:
             print("True")