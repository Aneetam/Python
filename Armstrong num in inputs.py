N=int(input())
for i in range(N):
    num=int(input())
    num_str=str(num)
    power=len(num_str)
    armstrong_sum=sum(int(digit)**power for digit in num_str)
    if(armstrong_sum==num):
        print(num)