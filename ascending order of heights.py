# a=[int(i) for i in input().split()]
a=list(map(int,input().split()))
arr=sorted(a)
c=0
for i in range(len(a)):
    if arr[i]!=a[i]:
        c+=1
print(c)