# def collatz(n):
# 	if n == 1:
# 		return '1'
# 	if n % 2  :
# 		_n = 3*n +1
# 	else:
# 		_n = n//2
# 	return str(n) + " " + collatz(_n)
# n = int(input())
# print(collatz(n))

l=[]
n=int(input())
l.append(n)
while(n!=1):
    if(n%2==0):
        n1=n//2
        n=n1
        l.append(n1)
    else:
        n1=n*3+1
        n=n1
        l.append(n1)
print(l)