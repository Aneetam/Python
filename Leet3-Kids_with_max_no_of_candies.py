def kidsWithCandies(candies, extraCandies):
    max_candies = max(candies)  # Find the current maximum candies among all kids
    return [(candy + extraCandies) >= max_candies for candy in candies]  # Check each kid

# Taking input from the user
candies = list(map(int, input("Enter candies list (comma-separated): ").split(',')))
extraCandies = int(input("Enter the number of extra candies: "))

# Calling the function and printing the result
result = kidsWithCandies(candies, extraCandies)
print("Output:", result)

#input 
#12,1,12
#10