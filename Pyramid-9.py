N=int(input())
for i in range(1,N+1):
    left_dot=N-i
    zero=2*i-1
    print(". "*left_dot+"0 "*zero+". "*left_dot)