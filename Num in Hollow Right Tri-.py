n=int(input())
for i in range(1,n+1):
    if(i==1):
        row=""
        row+="1"
        print(row,end="")
        print()
        
    elif(i==n):
        for j in range(1,n+1):
            print(j,end=" ")
    else:
        row=""
        number=i
        middle_space=(2*(i-2)+1)
        row+="1"+(" ")*middle_space+str(number)+" "
        print(row)