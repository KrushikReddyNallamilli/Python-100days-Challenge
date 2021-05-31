n=int(input())
even=0
odd=0
while(n>0):
	rem=n%10
	if(rem%2==0):
		even+=1
	else:
		odd+=1
	n=n//10
if(even>0 and odd>0):
	print("mixed")
elif(even>0 and odd==0):
	print("Strongly even")
elif(even==0 and odd==0):
	print("Please enter a number greater than 0")
else:
	print("Strongly odd")
