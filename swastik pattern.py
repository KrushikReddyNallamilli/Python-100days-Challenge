# n=5
# for i in range(1,2*n): #(1,2,3,4,5)
#     for j in range(1,2*n): #(1,2,3,4,5)
#         if i==n or j==n:
#             print('*', end='')
#         elif i< n and j==1:
#             print('*', end='')
#         elif i==1 and j >n:
#             print('*', end='')
#         elif i>n and j==2*n-1:
#             print('*', end='')
#         elif i==2*n-1 and j< n:
#             print('*', end='')
#         else: print(' ', end='')
#     print()



# def Swasthik(n):

#     for i in range(0,n):
#         for j in range(0,n):
#             if (i<n//2 and j==0) or (i==n//2) or(i>n//2 and j==n-1) or (j==n//2) or (i==0 and j>n//2) or (i==n-1 and j<n//2) :
#                 print("*",end="")
#             else:
#                 print(" ",end="")
#         print()
# n=5
# Swasthik(n)

n=int(input())

for i in range(1,2*n):
    for j in range(1,2*n):
        if(i==n or j==n):
            print("*",end="")

        elif(i==n//n and j>n):
            print("*",end="")
        elif(i<n and j==n//n):
            print("*",end="")
        elif(i>n and j==2*n-1):
            print("*",end="")
        elif(i==2*n-1 and j<n):
            print("*",end="")
        else:
            print(" ",end="")
    print()



# *   *****
# *   *
# *   *
# *   *
# *********
#     *   *
#     *   *
#     *   *
# *****   *
