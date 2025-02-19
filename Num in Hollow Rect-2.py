M=int(input())
N=int(input())
num=1
for i in range(1,M+1):
    if i==1 or i==M:
        for j in range(N):
            print(num,end=" ")
            num+=1
    else:
        first_num=num
        num+=N-1
        last_num=num
        print(first_num,end=" ")
        print(" " *(2*(N-2)),end="")
        print(last_num,end=" ")
        num+=1
    print()