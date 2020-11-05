# Given an integer array arr of distinct integers and an integer k.

# A game will be played between the first two elements of the array (i.e. arr[0] and arr[1]). In each round of the game, we compare arr[0] with arr[1], the larger integer wins and remains at position 0 and the smaller integer moves to the end of the array. The game ends when an integer wins k consecutive rounds.

# Return the integer which will win the game.

# It is guaranteed that there will be a winner of the game.

 

# Example 1:

# Input: arr = [2,1,3,5,4,6,7], k = 2
# Output: 5
# Explanation: Let's see the rounds of the game:
# Round |       arr       | winner | win_count
#   1   | [2,1,3,5,4,6,7] | 2      | 1
#   2   | [2,3,5,4,6,7,1] | 3      | 1
#   3   | [3,5,4,6,7,1,2] | 5      | 1
#   4   | [5,4,6,7,1,2,3] | 5      | 2
# So we can see that 4 rounds will be played and 5 is the winner because it wins 2 consecutive games.
# Example 2:

# Input: arr = [3,2,1], k = 10
# Output: 3
# Explanation: 3 will win the first 10 rounds consecutively.
# Example 3:

# Input: arr = [1,9,8,2,3,7,6,4,5], k = 7
# Output: 9
# Example 4:

# Input: arr = [1,11,22,33,44,55,66,77,88,99], k = 1000000000
# Output: 99
 

# Constraints:

# 2 <= arr.length <= 10^5
# 1 <= arr[i] <= 10^6
# arr contains distinct integers.
# 1 <= k <= 10^9


a=[2,1,3,5,4,6,7]
k=2
p,l=0,0
for i in range(len(a)):
	if a[0]<a[1]:
		p=a[1]
		a.append(a[0])
		a.remove(a[0])
	else:
		if p==a[0]:
			l+=1
		else:
			l=1
			p=a[0]
			a.remove(a[1])
			a.append(a[1])
		if l==k:
			break
print(a[0],l,i+1)



# --------------------------------------
# a=list(map(int,input().split()))
# n=int(input())
# c=0
# count=0
# d=-1
# while(c<(n+len(a))):
#     if a[0]>a[1]:
#         b=a[1]
#         c=a[0]
#         a.remove(b)
#         a.append(b)
#     else:
#         b=a[0]
#         c=a[1]
#         a.remove(b)
#         a.append(b)
#     if c==d:
#         count+=1
#         if count==n:
#             print(c,a)
#             break
#     else:
#         count=1
#         d=c
#     c+=1


# ===========================================
# arr=list(map(int,input().split()))
# k=int(input())
# d={}
# for i in range(len(arr)):
#     c=0
#     if arr[0]>arr[1]:
#         c=arr[1]
#         if arr[0] in d:
#             d[arr[0]]+=1
#         else:
#             d[arr[0]]=1
#         arr.remove(arr[1])
#         arr.append(c)
#     elif arr[0]<arr[1]:
#         c=arr[0]
#         if arr[1] in d:
#             d[arr[1]]+=1
#         else:
#             d[arr[1]]=1
#         arr.remove(arr[0])
#         arr.append(c)
# for i in d:
#     if d[i]==k:
#         print(i)
#         break
# -------------------------------------------
# Wrong solution
# arr=list(map(int,input().split()))
# k=int(input())
# c=0
# n=0
# for i in arr:
# 	if arr[0]>arr[1]:
# 		arr.append(arr[1])
# 		arr.remove(arr[1])
# 		c+=1
# 	elif arr[0]<arr[1]:
# 		arr.append(arr[0])
# 		arr.remove(arr[0])
# 		c+=1
# 	if c==k:
# 		print(arr[0]) Wrong