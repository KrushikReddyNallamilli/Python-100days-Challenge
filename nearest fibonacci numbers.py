def nearfib(n):
	a,b=0,1
	while n>=b:
		c=a+b
		a=b
		b=c
	if abs(b-n)>abs(a-n):
		return a
	return b
print(nearfib(int(input())))



# def nearfib(n):
# 	a,b=0,1
# 	while n>b:
# 		a,b=b,a+b
# 	return(a)
# print(nearfib(int(input())))


# def nearfib(n):
# 	a,b=0,1
# 	while n>=b:
# 		c=a+b
# 		a=b
# 		b=c
# 	return("Nearest fibonacci number (previous) is",a)
# print(nearfib(int(input())))

# def nearfib(n):
# 	a,b=0,1
# 	while n>=b:
# 		c=a+b
# 		a=b
# 		b=c
# 	return("Nearest fibonacci number is",b)
# print(nearfib(int(input())))

# def fib(n):
#     if n==1:
#         return 0
#     elif n==2:
#         return 1
#     else:
#         return (fib(n-1)+fib(n-2))
# num=int(input())
# for i in range(1,num):
#     k=fib(i)
#     if k==num:
#         print(num)
#         break
#     if k>num:
#         print("next",fib(i))
#         break

# def fib(n):
#     if n==1:
#         return 0
#     elif n==2:
#         return 1
#     else:
#         return (fib(n-1)+fib(n-2))
# num=int(input())
# for i in range(1,num):
#     k=fib(i)
#     if k==num:
#         print(num)
#         break
#     if k>num:
#         print("previous",fib(i-1))
#         break


