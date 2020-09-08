# beatty sequence

# n=5
# n*sqrt(2)

# 1 2 4 5 7
# 1*sqrt(2)=1*1.414=1
# 2*sqrt(2)=2*1.414=2
# 3*sqrt(2)=3*1.414=4
# 4*sqrt(2)=4*1.414=5
# 5*sqrt(2)=5*1.414=7
# # 6*sqrt(2)=6*1.414=8


import math
def beatty_seq(n):
	for i in range(1,n+1):
		print(math.floor(i*math.sqrt(2)),end=" ")
n=int(input())
beatty_seq(n)