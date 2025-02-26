def find_last_occurrence(lst, N):
    last_index = -1  # Initialize last_index to -1 (default if N is not found)
    
    for i in range(len(lst)):  # Loop through all indices of the list
        if lst[i] == N:  # If the current element matches N
            last_index = i  # Update last_index to the current index
    
    return last_index  # Return the last found index (or -1 if not found)

#####
#def find_last_occurrence(lst, N):
    try:
        return len(lst) - 1 - lst[::-1].index(N)
    except ValueError:
        return -1  # Return -1 if N is not found

# Example usage
numbers = [1, 2, 3, 4, 2, 5, 2, 6]
N = 2
#print(find_last_occurrence(numbers, N))  # Output: 6