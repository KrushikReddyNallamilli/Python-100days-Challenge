n=int(input("Enter a number: "))
sr=int(input("Enter the starting range: "))
er=int(input("Enter the ending range: "))

if(sr>er):
	for i in range(sr,er-1,-1):
		print(n,'*',i,'= ',n*i)
else:
	for i in range(sr,er+1):
		print(n,'*',i,'= ',n*i)

