def print_sandglass(n):
    # Upper half of the sandglass
    for i in range(n, 0, -1):
        print(" " * (n - i) + "* " * i)

    # Lower half of the sandglass
    for i in range(2, n + 1):
        print(" " * (n - i) + "* " * i)

# Take user input
N = int(input())
print_sandglass(N)