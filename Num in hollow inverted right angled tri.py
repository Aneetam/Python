S=int(input())
N=int(input())
for i in range(1,N+1):
    if(i==1):
        for j in range(N):
            print(S,end=" ")
            S+=1
        print()
    elif(i==N):
        space=i-1
        print("  "*space+str(S),end="")
        S+=1
    else:
        print("  " *(i-1)+str(S),end="")
        S+=1
        print(" "*((2*(N-i))-2),S)
        S+=1