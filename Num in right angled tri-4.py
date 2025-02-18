S=int(input())
N=int(input())
num=S
for i in range(1,N+1):
    for j in range(2*i):
        print(num,end=" ")
        num+=1
    print()