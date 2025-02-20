N=int(input())
for i in range(1,2*N):
    if i==1 or i==N or i==2*N-1:
        print("* " *N)
        
    elif(i<N):
        left_space=N-1
        print("  "*left_space+("* "))
    else:
        right_space=N-1
        print("* "+(" ")*right_space)