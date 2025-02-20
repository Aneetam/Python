N = int(input())

# Upper half
for i in range(N, 0, -1):
    for j in range(1, i + 1):
        print(chr(64 + j), end=" ")  # Convert number to ASCII character (A = 65)
    print()