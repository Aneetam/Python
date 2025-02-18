N=int(input())
for M in range(1,N+1):
    for i in range(1,M+1):
        print(i,end=" ")
    for i in range(1,M):
        print(i,end=" ")
    print()