n=int(input())
for i in range(1,n+1):
    if(i==1):
        print("* " *n)
    elif(i==n):
        row="* "
        print(row)
    else:
        space=n-i-1
        row=("* ")+("  ")*space+("* ")
        print(row)