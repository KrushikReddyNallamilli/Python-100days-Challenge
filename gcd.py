# import math
# def gcd(num1,num2):
#     return math.gcd(num1,num2)
# num1,num2=map(int,input("enter numbers").split())
# print(gcd(num1,num2))



# n,m=map(int,input("enter numbers").split())
# if n>m:
# 	small=m
# else:
# 	small=n
# for i in range(1,small+1):
# 	if(n%i==0 and m%i==0):
# 		gcd=i
# print(gcd)


a = int(input("First Number :"))
b = int(input("Second Number :"))
i = 1
gcd = 1
while i<=min(a,b):
	if a%i==0 and b%i==0 :
		gcd = i
	i+=1
print(gcd)