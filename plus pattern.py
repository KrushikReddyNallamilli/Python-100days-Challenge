# n=7
# x=1
# for i in range (0,n+1):
# 	for j in range(i,x):
# 		#print("i in j=",i)
# 		print(("*"*1).center(n*n))
# 	x+=1
# print(i)

n = int(input('Enter value of n: ')) #3
for i in range(1,2*n): #(1,2,3,4,5)
    for j in range(1,2*n): #(1,2,3,4,5)
        if i==n or j==n:
            print('*', end='')
        else:
            print(' ', end='')
    print()

#   *
#   *
# *****
#   *
#   *