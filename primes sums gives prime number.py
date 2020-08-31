# def prime(n):
#     for i in range(2,n):
#         if(n%i==0):
#             break
#     else:
#         return(1)

# num = int(input("Enter a number : "))
# flag = 0;
# if (prime(num)==1):
# 	i = 2
# 	for i in range (2,int(num/2),1):
# 	    if(prime(i) == 1):
# 	        if(prime(num-i) == 1):
# 	            print(num,"can be expressed as the sum of",i,"and",num-i)
# 	            flag = 1;
# 	if (flag == 0):
# 	    print(n,"cannot be expressed as the sum of two prime numbers")


def prime(n):
    for i in range(2,n):
        if(n%i==0):
            break
    else:
        return n

def primesum(n):
	if (prime(n)+prime(n-2)):
		return(n-2,2)
n=int(input("Enter a number"))
print(primesum(n))


# eg 19,13 