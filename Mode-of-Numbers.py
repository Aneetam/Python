numbers=list(map(int,input().split(",")))
max_freq=max(numbers.count(num) for num in numbers)
modes=list(set(num for num in numbers if numbers.count(num)==max_freq))
print(" ,".join(map(str,modes)))