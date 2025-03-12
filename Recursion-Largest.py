def get_largest_square(numbers):
    # Complete this function
    if not numbers:
        return 0
    current_square=int(numbers[0])**2
    max_square=get_largest_square(numbers[1:])
    return max(current_square,max_square)
    


numbers = input().split()

result = get_largest_square(numbers)
print(result)