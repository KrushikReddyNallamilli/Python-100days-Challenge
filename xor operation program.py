# n,start = map(int,input().split())
# xor = 0
# for j in range(start,2*n + start,2):
# 	xor ^= j
# print(xor)

n=int(input())
start=int(input())
x=0
for i in range(n):
    x=x^(start+2*i)
print(x)