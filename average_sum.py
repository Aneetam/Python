M=int(input())
N=int(input())
sum_of_num=0
average_num=0
for num in range(M,N+1):
    sum_of_num+=num
print(sum_of_num)
length=N-M+1
average_num=sum_of_num/length
print(average_num)

    