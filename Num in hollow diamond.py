N=int(input())
for i in range(1,N+1):
    if(i==1):
        space=(N-i)
        print(" "*space+str(i),end=" ")
        print()
        
    else:
        left_space=N-i
        middle_space=2*i-3
        row=(" ")*left_space+str(1)+(" ")*middle_space+str(i)+" "
        print(row)
for i in range(1,N):
    if(i==N-1):
        space=(i)
        print(" "*space+str(1))
        
    else:
        left_space=i
        middle_space=2*(N-i-2)+1
        num=N-i
        row=(" ")*left_space+str(1)+(" ")*middle_space+str(num)
        print(row)