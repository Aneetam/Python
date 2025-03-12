numbers=input()
k=int(input())
num_list=[int(num) for num in numbers.split(",")]
num_list.sort(reverse=True)
print(num_list[k-1])