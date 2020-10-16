# Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.
# Note that elements beyond the length of the original array are not written.
# Do the above modifications to the input array in place, do not return anything from your function.
 
# Example 1:
# Input: [1,0,2,3,0,4,5,0]
# Output: null
# Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
# Example 2:
# Input: [1,2,3]
# Output: null
# Explanation: After calling your function, the input array is modified to: [1,2,3]
 
# Note:
# 1 <= arr.length <= 10000
# 0 <= arr[i] <= 9

# a=list(map(int,input().split()))
# l=[]
# for i in range(len(a)):
# 	if a[i]==0:
# 		l.append(a[i])
# 		l.append(0)
# 	else:
# 		l.append(a[i])
# print(l[:len(a)])



l=list(map(int,input().split()))
c=0
le=len(l)
for i in range(le):
    if l[c]==0:
        l.insert(c+1,0)
        c+=1
    c+=1
print(l[:le])