s = "Anjali25 is python4 Expert"

# Extract numbers manually
num = ""
numbers = []
for char in s:
    if char.isdigit():
        num += char  # Build the number
        print(char)
    elif num:
        print(num)
        numbers.append(int(num))  # Store completed number
        num = ""  # Reset for next number

if num:  # Add last collected number if exists
    numbers.append(int(num))

# Calculate sum and average
total_sum = sum(numbers)
average = round(total_sum / len(numbers), 2) if numbers else 0  # Avoid division by zero

# Output results
print("Sum:", total_sum)
print("Average:", average)