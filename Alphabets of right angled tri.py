N=int(input())
for i in range(1,N+1):
    space=(N-i)*2
    print(" "*space,end="")
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()