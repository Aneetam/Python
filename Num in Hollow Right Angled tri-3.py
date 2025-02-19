S=int(input())
N=int(input())
num=S
for i in range(1,N+1):
    for j in range(1,N+1):
        if j==1 or i==j or i==N:
            print(num,end=" ")
            num+=1
        else:
            print(" ",end=" ")
    print()