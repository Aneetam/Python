n=int(input())
for i in range(1,n+1):
    if(i==1):
        row=""
        space=n-1
        row+=("  ")*space+"1 "
        print(row)
    elif(i==n):
        for j in range(n,0,-1):
            print(j,end=" ")
    else:
        row=""
        left_space=n-i
        middle_space=i-2
        row+=("  ")*left_space+str(i)+" "+("  ")*middle_space+"1 "
        print(row)