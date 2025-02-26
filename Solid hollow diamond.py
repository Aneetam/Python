n=int(input())
for i in range(1,n+1):
    spaces=n-i
    star=i
    row=(" ")*spaces+("* ")*star
    print(row)
for i in range(1,n):
    if(i==n-1):
        left_space=n-1
        row=(" ")*left_space+("*")
        print(row)
    else:
        left_spaces=i
        hollow_space=2*(n-i)-3
    
        row=(" ")*left_spaces+("*")+(" ")*hollow_space+("*")
        print(row)