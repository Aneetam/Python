numbers=input()
num_list=[int(num) for num in numbers.split(",")]
num_list.sort(reverse=True)
max_sum=sum(num_list[:5])
print(max_sum)