from datetime import datetime, timedelta

# Taking input from the user
date_str = input().strip()  # First line: date (e.g., 'Jan 28 2021')
years_to_add = int(input().strip())  # Second line: years to add/subtract

# Converting input date to a datetime object
date_obj = datetime.strptime(date_str, "%b %d %Y")

# Adding/subtracting Y years as 365 days per year
new_date = date_obj + timedelta(days=365 * years_to_add)

# Formatting output
formatted_new_date = new_date.strftime("%Y-%m-%d %H:%M:%S")

# Printing the result
print(formatted_new_date)