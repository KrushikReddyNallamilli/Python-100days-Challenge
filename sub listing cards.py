
# # def deckpairs(arr):
# #     pairs = sorted([arr.count(i)  for i in set(arr)])
# #     return all([i%pairs[0]== 0 for i in pairs]) and pairs[0]>1
# # arr = list(map(int,input().split()))
# # print(deckpairs(arr))

# some test cases failed

def pattern(l):
	d={ }
	for i in l:
		d[i]=d.get(i,0)+1
	val=d.values()
	for i in range(2,min(val)+1):		
		if sum([0 if v%i==0 else l for v in val])==0:
			return True
	return False
l=[1,2,2,2,2,1,3,3,3,3,3,3]
print(pattern(l))

# print("i=",i)
		# print("minval=",min(val))
# Question

# In a deck of cards, each card has an integer written on it.
# Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:
# Each group has exactly X cards.
# All the cards in each group have the same integer.
 
# Example 1:
# Input: deck = [1,2,3,4,4,3,2,1]
# Output: true
# Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].
# Example 2:
# Input: deck = [1,1,1,2,2,2,3,3]
# Output: false´
# Explanation: No possible partition.
# Example 3:
# Input: deck = [1]
# Output: false
# Explanation: No possible partition.
# Example 4:
# Input: deck = [1,1]
# Output: true
# Explanation: Possible partition [1,1].
# Example 5:
# Input: deck = [1,1,2,2,2,2]
# Output: true
# Explanation: Possible partition [1,1],[2,2],[2,2].
 
# Constraints:
# 1 <= deck.length <= 10^4
# 0 <= deck[i] < 10^4