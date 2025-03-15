def find_missing_numbers(numbers):
    complete_set=set(range(1,max(numbers)+1))
    input_set=set(numbers)
    missing_numbers=complete_set - input_set
    return sorted(missing_numbers)




numbers=list(map(int,input().split()))
missing_numbers=find_missing_numbers(numbers)
print(missing_numbers)