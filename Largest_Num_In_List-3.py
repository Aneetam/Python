numbers=input().split(",")
index=int(input())
num_list=[int(num) for num in numbers]
index_list=num_list[index:]
max_num=max(index_list)
print(max_num)