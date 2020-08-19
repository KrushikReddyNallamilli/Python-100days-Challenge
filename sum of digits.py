# def sum(n):
# 	s=0
# 	while n!=0:
# 		rem=n%10
# 		s=s+rem
# 		n=n//10
# 	return(s)
# n=int(input())
# print(sum(n))



# n=input()
# l=[]
# for i in n:
# 	l.append(int(i))
# print(sum(l))



# def  sum_digits(n):
# 	s=0
# 	while n>0:
# 		rem=n%10
# 		s=s+rem
# 		n=n//10
# 	return s
# n=int(input("Enter a number: "))
# print(sum_digits(n))




n=input("Enter a number: ")
s=0
for i in n:
	s+=int(i)
print(s)