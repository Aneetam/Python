def get_even_numbers_count(numbers):
    # complete this function
    count=0
    for num in numbers:
        if num%2==0:
            count+=1
    return count


numbers = list(map(int,input().split()))
result = get_even_numbers_count(numbers)
print(result)