n=int(input())
for i in range(n,0,-1):
    if(i==n):
        for j in range(1,n+1):
            print(j,end=" ")
        print()
    elif(i==1):
        print("1")
    else:
        print("1",end=" ")
        spaces=(2*(i-2))*" "
        print(spaces,end="")
        print(i)