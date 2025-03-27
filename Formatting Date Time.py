from datetime import datetime

# Take input from the user
date_str = input("Enter a date (e.g., 'Jul 01 2014 02:43 PM'): ")

# Convert the string into a datetime object
date_obj = datetime.strptime(date_str, "%b %d %Y %I:%M %p")

# Format the datetime object into the desired output format
formatted_date = date_obj.strftime("%d/%m/%Y %H:%M:%S")

# Print the formatted date
print(date_obj)
print("Formatted Date:", formatted_date)