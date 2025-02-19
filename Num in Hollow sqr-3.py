S=int(input())
N=int(input())
for i in range(N):
    for j in range(N):
        if i==0 or i==N-1 or j==0 or j==N-1:
            print(S,end=" ")
        else:
            print(" ",end=" ")
        S+=1
    print()