S=int(input())
N=int(input())
for i in range(1,N+1):
    if i==1:
        for j in range(1,N+1):
            print(S,end=" ")
            S+=1
        print()
    elif i==N:
        print(" "*(N-1)+str(S))
    else:
        left_space=i-1
        middle_space=2*(N-i-1)
        print(" "*left_space,end="")
        print(S,end=" ")
        S+=N-i
        print(" "*middle_space,end="")
        print(S)
        S+=1