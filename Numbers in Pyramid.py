S=int(input())
N=int(input())
for i in range(N):
    num=S
    spaces=N-i-1
    print(" "*spaces,end="")
    for j in range(i+1):
        print(num,end=" ")
        num+=1
    print()