##a=int(input("Enter from value"))
##b=int(input("Enter from value"))
##for i in range(a,b+1):
##    if(i%3==0):
##        print(i,end=",")

# a=int(input("Enter from value"))
# b=int(input("Enter from value"))
# i=a
# while(i>=a and i<=b):
#     if(i%3==0):
#         print(i,end=" ")
#     i=i+1

a=int(input("Enter from value"))
b=int(input("Enter from value"))
while True:
	if (a%3==0):
		print(a,end=0)
	a+=1
	if a>b:
		break

