def sum_of_triangle(arr):
    triangle = [arr]  # Store the original row
    
    # Generate the sum triangle rows
    while len(arr) > 1:
        new_row = []  # To store the next row
        for i in range(len(arr) - 1):
            new_row.append(arr[i] + arr[i + 1])  # Sum adjacent elements
        triangle.append(new_row)  # Add the new row to the triangle
        arr = new_row  # Update arr for the next iteration
    
    # Print the triangle
    for row in triangle:
        print(row)

# Input
sum_of_triangle([1, 2, 3])