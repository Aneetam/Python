N=int(input())
S=1
for i in range(1,N+1):
    if i==1:
        for j in range(N,0,-1):
            print(S,end=" ")
            S+=1
        print()
    elif i==N:
        print(S)
        S+=1
    else:
        print(S,end=" ")
        middle_space=2*(N-i-1)
        print(" " *middle_space,end="")
        S+=N-i
        print(S)
        S+=1