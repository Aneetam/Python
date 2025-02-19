M=int(input())
N=int(input())
K=M*N
for i in range(1,M+1):
    if i==1 or i==M:
        for j in range(N):
            print(K,end=" ")
            K-=1
    else:
        first_num=K
        K-=N-1
        last_num=K
        print(first_num,end=" ")
        print(" "*(2*(N-2)),end="")
        print(last_num,end=" ")
        K-=1
    print()