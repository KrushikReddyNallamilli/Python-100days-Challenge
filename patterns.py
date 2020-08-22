# Patterns

# Pattern1

# n=int(input('Enter a number'))
# for i in range(1,n+1):
# 	for j in range(1,n+1):
# 		print(j,end=" ")
# 	print()


# output
# Enter a number5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

#--------or-----------------
# for i in range(5):
# 	print("1 2 3 4 5")

#--------------------------
# Pattern2

# n=int(input('Enter a number'))
# for i in range(1,n+1):
# 	for j in range(1,n+1):
# 		print(i,end=" ")
# 	print()
# Output
# 1 1 1 1 1 1
# 2 2 2 2 2 2
# 3 3 3 3 3 3
# 4 4 4 4 4 4
# 5 5 5 5 5 5
# 6 6 6 6 6 6

#------------------------------------
# Pattern3
# num=int(input('enter the number of rows :'))
# for i in range(1,num+1):
#           print(i * '* ')

# Output
# enter the number of rows :5
# *
# * *
# * * *
# * * * *
# * * * * *
# ----------or--------

n=int(input('Enter a number'))
for i in range(1,n+1):
	for j in range(i):
		print("*",end=" ")
	print()

#---------------------------------