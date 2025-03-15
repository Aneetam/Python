def remove_non_numbers(input_list):
    # Filter out only numeric elements (integers or floats)
    numeric_list = [int(x) for x in input_list if x.lstrip('-').isdigit()]
    return numeric_list

# Taking input from the user
input_list = input().split(",")

# Get the result with only numbers
result = remove_non_numbers(input_list)

# Output the result
print("List with only numbers:", result)