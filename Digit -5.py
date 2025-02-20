N=int(input())
for i in range(1,2*N):
    if i==1 or i==N or i==2*N-1:
        print("* "*N)
    elif(i<N):
        print("*")
    else:
        print("  "*(N-1)+("*"))