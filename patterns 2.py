#     0
#    101
#   21012
#  3210123
# 432101234

n=5
x=1
for i in range(1,n+1): #1,2,3,4,5
	for j in range(n,i,-1): #5,4,3,2,1
		print(' ',end="")
	for k in range(1,x+1): #(1),(1,2,3)
		print(abs(k-i),end="") #(1-1),(1,0,1)
	x=x+2
	print()