N=int(input())
K=0
num=0
for k in range(1,N+1):
    K+=k
num=K

for i in range(N):
    
    space=i
    print("  " *space,end="")
    for j in range(N-i):
        print(num,end=" ")
        num=num-1
    print()