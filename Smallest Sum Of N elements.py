numbers=input().split(",")
N=int(input())
num_list=sorted([int(num) for num in numbers])
small_sum=sum(num_list[:N])
print(small_sum)