M=int(input())
N=int(input())
char=ord('A')
for i in range(M):
    for j in range(N):
        if i==0 or i==M-1 or j==0 or j==N-1:
            print(chr(char),end=" ")
        else:
            print(" ",end=" ")
        char+=1
    print()