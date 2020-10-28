
# input:
# n=6
# arr=1 0 1 0 1 1 
# output =2 max number of repetetive 1's are 2

def consec(arr, n): 
    c= 0 
    res = 0 
    for i in range(0, n): 
        if (arr[i] == 0): 
            c = 0
        else: 
            c+= 1
            print(c)
            res = max(res,c)            
    return res  

n=int(input())
arr=list(map(int,input().split()))
print(consec(arr,n))
