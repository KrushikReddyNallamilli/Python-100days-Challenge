# def fun(year):
# 	if year%4==0:
# 		if year%100!=0:
# 			if(year%400):
# 				print("Leap year")
# 			else:
# 				print("NOt Leap year")
# 		else:
# 			print("Leap")
# 	else:
# 		print("not a Leap")
# year=int(input("Enter a year"))
# fun(year)


def fun1(year):
	if year%4==0 and year%100!=0 or year%400==0:
		return("Leap")
	else:
		return("NOt a Leap")
year=int(input("Enter a year"))
print(fun1(year))