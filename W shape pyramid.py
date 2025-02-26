n = int(input())

# First row
print("* " * (2 * n - 1))

# Subsequent rows
for i in range(1, n):
    first_space = i
    first_star = n - i
    space_between = (2 * i) - 2 # Calculate middle spaces based on current row index
    star = n - i
    
    # Constructing each part of the row
    left_spaces = " " * first_space
    left_stars = "* " * first_star
    middle_spaces = " " * space_between 
    right_stars = "* " * star
    
    # Combining all parts to form the complete row string
    row = left_spaces + left_stars + middle_spaces + right_stars
    
    print(row)