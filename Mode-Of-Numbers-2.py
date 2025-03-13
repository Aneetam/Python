# Read input: comma-separated numbers
numbers = list(map(int, input("Enter numbers separated by commas: ").split(",")))

# Find the maximum frequency using count()
max_freq = max(numbers.count(num) for num in numbers)

# Get the first number that has the maximum frequency
for num in numbers:
    if numbers.count(num) == max_freq:
        print("Mode:", num)
        break
