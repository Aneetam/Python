def productExceptSelf(nums):
    n = len(nums)
    answer = [1] * n  # Step 1: Initialize answer array

    # Step 2: Compute prefix products
    prefix = 1
    for i in range(n):
        answer[i] = prefix  # Store prefix product
        prefix *= nums[i]   # Update prefix for next iteration

    # Step 3: Compute suffix products
    suffix = 1
    for i in range(n - 1, -1, -1):  # Right to left
        answer[i] *= suffix  # Multiply with suffix product
        suffix *= nums[i]     # Update suffix for next iteration

    return answer

# Taking input from user
nums = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Function call and printing the result
print("Output:", productExceptSelf(nums))