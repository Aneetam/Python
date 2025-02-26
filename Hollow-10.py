n=int(input())
for i in range(1,n+1):
    if(i==1):
        hollow_space=2*n-2
        row=("* ")+("  ")*hollow_space+("*")
        print(row)
    elif(i==n):
        star=2*n
        row=("* ")*star
        print(row)
    else:
        left_space=i-2
        hollow_space=2*(n-i)
        right_space=i-2
        row=("* ")+("  ")*left_space+("* ")+("  ")*hollow_space+("* ")+("  ")*right_space+("* ")
        print(row)