n = int(input())  # Read the first input as an integer (number of elements)
numbers = list(map(int, input().split()))  # Read the list of numbers

half_length = (n + 1) // 2  # Calculate half length (rounding up)
result = numbers[-half_length:]  # Get the last half of the list

print(result)  # Print the result as a list