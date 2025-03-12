numbers=input()
input_list=[int(num) for num in numbers.split(",")]
input_list.sort(reverse=True)
print(input_list)