def find_missing_positive(nums):
    # Step 1: Keep only positive numbers
    positive_nums = set()  # Use a set for faster lookup
    for num in nums:
        if num > 0:
            positive_nums.add(num)

    # Step 2: Find the smallest missing positive number
    smallest = 1  # Start checking from 1
    while smallest in positive_nums:  # If found in set, move to next
        smallest += 1

    return smallest  # The first missing positive integer

# Take input as a list of space-separated integers
nums = list(map(int, input().split()))

# Print the missing smallest positive number
print(find_missing_positive(nums))