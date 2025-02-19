n=int(input())
s=int(input())
end=s+n
for i in range(1,n+1):
    if(i==1):
        for j in range(s,end):
            print(j,end=" ")
    elif(i==n):
        space=n-1
        print(" "*space+"7 ",end="")
    else:
        row=""
        left_space=i-1
        middle_space=(2 *(n-i-1))
        num=s+(n-i)
        row+=(" ")*left_space+str(s)+" "+(" ")*middle_space+str(num)+" "
        print(row)
    print()