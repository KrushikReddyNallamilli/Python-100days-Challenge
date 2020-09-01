# def pattern(n):
#       k = 2 * n - 2
#       for i in range(0,n):
#            for j in range(0,k):
#                print(end=" ")
#            k = k - 1
#            for j in range(0, i+1):
#                 print("*", end=" ")
#            print(" ")
 
# pattern(5)



# def pattern(n):
# 	for i in range(n,-n,-1):
# 		for j in range(1,abs(i)+1):
# 			print(' ',end='')
# 		for k in range(n,abs(i),-1):
# 			print("* ",end="")
# 		print()
# n=int(input())
# pattern(n)

def pattern(n):
	for i in range(n):
		print(("* "*(i+1)).center(2*n))
	for i in range(n-1,0,-1):
		print(("* "*(i)).center(2*n))
n=int(input())
pattern(n)
