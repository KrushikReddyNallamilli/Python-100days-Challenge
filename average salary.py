# a=[4000,3000,1000,5000]
# a.sort()
# b=a[1:len(a)-1]
# print(sum(b)/len(b))

l=[2,3,3,5]
l.remove(min(l))
l.remove(max(l))
print(sum(l)//len(l))