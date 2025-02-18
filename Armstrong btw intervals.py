M=int(input())
N=int(input())
flag=True
for num in range(M,N+1):
    sum_of_digits=0
    num_str=str(num)
    power=len(num_str)
    for digit in num_str:
        sum_of_digits+=int(digit) **power
    if(sum_of_digits==num):
        flag=False
        print(num,end=" ")
if flag:
    print("-1")