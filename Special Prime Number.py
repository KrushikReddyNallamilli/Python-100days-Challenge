'''
Special Prime:
19

17 13 --->  17+13+1
13 11 --->  13+11+1
11 7  --->  11+7+1
'''


import math
def prime(n):
    for i in range(2,abs(int(math.sqrt(n)))+1):
        if n%i==0:
            break
    else:
        return(1)
n=int(input("enter a number:"))
def near_prime(n):
    n1=n-1
    while True:
        if prime(n1):
            return n1
        else:
            n1-=1


if prime(n):
	
    a=near_prime(n)
    b=near_prime(a)
    while True:
        if a+b+1==n:
            print(a,b)
            print(n, "is a special prime")
            break
        else:
            a=b
            b=near_prime(a)
        if a==2 or b==2:
            break
else:
    print("not a prime")



