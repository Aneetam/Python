n=int(input())
for i in range(1,n+1):
    if(i==1):
        print("* ")
    elif(i==n):
        print("* "*n)
    else:
        space=i-2
        row=("* ")+("  ")*space+("* ")
        print(row)