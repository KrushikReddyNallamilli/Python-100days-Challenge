# num=int(input('enter the number of rows :'))
# for i in range(num):
#           print(("* " *(num-i)).center(2*num))


# n=5
# for i in range(n,0,-1): #5,4,3,2,1
# 	for j in range(i,n):#(i=5,n=5)(5:0)
# 		print(" ",end="")
# 	for k in range(0,i):(0,5:0,1,2,3,4)
# 		print("* ",end="")
# 	print()


n=5
for i in range(n,0,-1):
    print(("* "*(i)).center(2*n))


# n=int(input())
# p=0
# for i in range(n,-1,-1):

# 	print(" "*p,end="")

# 	p+=1

# 	print("* "*i,end="")

# 	print()