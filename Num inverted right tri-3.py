S=int(input())
N=int(input())
K=0
for i in range(1,N+1):
    K+=i
num=K+S-1
for i in range(N):
    for j in range(N-i):
        print(num,end=" ")
        num=num-1
    print()