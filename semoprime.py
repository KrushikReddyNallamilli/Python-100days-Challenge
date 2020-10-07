import math 
def checkSemiprime(num): 
    cnt = 0

    for i in range(2, int(math.sqrt(num)) + 1): 
        while num % i == 0: 
            num /= i 
            cnt += 1 
        if cnt >= 2: 
            break
    if(num > 1): 
        cnt += 1
    return cnt == 2
def semiprime(n): 
    if checkSemiprime(n) == True: 
        print("NO") 
    else: 
        print("YES") 

lst = [] 
n = int(input()) 
for i in range(0, n): 
    ele = int(input()) 
    semiprime(ele) 