def print_hollow_diamond(n):
    # Upper part of the diamond
    for i in range(n):
        ch = chr(65 + i)  # Convert row index to corresponding alphabet (A, B, C...)
        for j in range(n - i - 1):
            print(" ", end=" ")  # Leading spaces
        
        for j in range(2 * i + 1):
            if j == 0 or j == 2 * i:  # Print only boundary characters
                print(ch, end=" ")
            else:
                print(" ", end=" ")
        
        print()  # Move to the next line
    
    # Lower part of the diamond
    for i in range(n - 2, -1, -1):
        ch = chr(65 + i)
        for j in range(n - i - 1):
            print(" ", end=" ")  # Leading spaces
        
        for j in range(2 * i + 1):
            if j == 0 or j == 2 * i:  # Print only boundary characters
                print(ch, end=" ")
            else:
                print(" ", end=" ")
        
        print()  # Move to the next line


# Input
N = int(input())
print_hollow_diamond(N)