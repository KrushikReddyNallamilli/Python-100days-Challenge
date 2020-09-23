# n=input()
# n=n[::-1]
# c=0
# sum1=0
# for i in n:
# 	sum1+=int(i)*8**c
# 	c+=1
# print(sum1)



# n=1111
# d=0
# b=1
# while n:
# 	r=n%10
# 	n=n//10
# 	d+=r*b
# 	b*=8
# print(d)

n=int(input())
c=0
for i in range(0,len(str(n))):
	rem=n%10
	c+=(rem* 8**i)
	n=n//10
print(c)
