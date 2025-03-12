numbers=input().split(",")
num_list=sorted([int(num) for num in numbers])
n=len(num_list)
if n%2==1:
    median_value=num_list[n // 2]
else:
    median_value=(num_list[n // 2-1]+num_list[n // 2])/2
print(median_value)