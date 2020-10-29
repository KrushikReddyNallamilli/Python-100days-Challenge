# import collections
# arr=list(map(int,input().split()))
# ctr = collections.Counter(arr)
# ctr[-1]= -1
# return(max([i for i in ctr if i == ctr[i]]))


def lucky(arr):
    counter = {}
    for i in arr:counter[i] = counter.get(i,0)+1
    lucky_integer = -1
    for val in sorted(set(arr),reverse = True):
       if val == counter[val]:
           return val;
    return lucky_integer;

arr = list(map(int,input().split()))
print(lucky(arr))