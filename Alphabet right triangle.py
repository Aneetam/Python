def print_pattern(n):
    for i in range(1, n + 1):
        # Print increasing sequence
        for j in range(1, i + 1):
            print(j, end="")
        # Print decreasing sequence
        for j in range(i - 1, 0, -1):
            print(j, end="")
        print()  # Move to the next line

# Get user input
n = int(input())
print_pattern(n)