N=int(input())
k=1
for i in range(1,N+1):
    dots=N-i
    zeros=k
    print(". "*dots+"0 " *zeros+". "*dots)
    k+=2
for i in range(N-1,0,-1):
    dots=N-i
    zeros=(2*N-1)-(dots*2)
    print(". "*dots+"0 " *zeros+". "*dots)