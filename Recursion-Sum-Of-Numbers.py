def get_sum(numbers):
    # Complete this recursive function
    if not numbers:
        return 0
    return int(numbers[0])+get_sum(numbers[1:])




numbers = input().split()

sum_of_numbers = get_sum(numbers)
print(sum_of_numbers)