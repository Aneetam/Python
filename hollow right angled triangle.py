n=int(input())
for i in range(1,n+1):
    if(i==1):
        print("* "*n)
    elif(i==n):
        space=i-1
        row=("  ")*space+("* ")
        print(row)
    else:
        hollow_space=(n-i-1)*2
        left_space=(i-1)
        
        row=("  ")*left_space+("* ")+(" ")*hollow_space+("* ")
        print(row)