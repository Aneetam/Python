n=int(input())
for i in range(1,n+1):
    if(i==1):
        print("# "*(n))
    elif(i==n):
        print("+")
    else:
        space=2*(n-i-1)
        row=("+ ")+(" ")*space+("+ ")
        print(row)