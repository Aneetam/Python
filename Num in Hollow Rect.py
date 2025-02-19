M=int(input())
N=int(input())
for i in range(M):
    for j in range(N):
        if(i==0 or i==M-1 or j==0 or j==N-1):
            print(7+j,end=" ")
            
        else:
            print("  ",end="")
    print()