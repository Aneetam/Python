n=int(input())
for i in range(1,n+1):
    if(i==1):
        spaces=(n-1)
        row=(" ")*spaces+("* ")
     
    elif(i==n):
        row=("* ")*n
        
    else:
        left_spaces=(n-i)
        hollow_spaces=2*i-4
        row=(" ")*left_spaces+("* ")+(" ")*hollow_spaces+("* ")
    print(row)