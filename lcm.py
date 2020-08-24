n,m=map(int,input("enter numbers").split())
greater=max(n,m)
while(True):
    if(greater%n==0 and greater%m==0):
        print("lcm=",greater)
        break
    greater+=1