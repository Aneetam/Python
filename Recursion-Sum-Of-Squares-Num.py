def get_sum_of_squares(numbers):
    # Complete this function by calling get_sum_of_squares function
    if not numbers:
        return 0
    return int(numbers[0])**2+get_sum_of_squares(numbers[1:])



    
numbers = input().split()

squares_sum = get_sum_of_squares(numbers)
print(squares_sum)