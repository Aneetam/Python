N=int(input())
for i in range(1,N+1):
    space=N-i
    print(" "*space,end="")
    for j in range(1,i+1):
        print(j,end=" ")
    print()
for i in range(1,N):
    space=i
    print(" "*space,end="")
    for j in range(1,N-i+1):
        print(j,end=" ")
    print()