from datetime import datetime, timedelta

# Taking input from the user
date_str = input("Enter a date (e.g., '26 Jan 2021'): ")

# Converting the input string to a datetime object
date_obj = datetime.strptime(date_str, "%d %b %Y")

# Calculating previous, current, and next day
prev_day = date_obj - timedelta(days=1)
next_day = date_obj + timedelta(days=1)

# Formatting output
formatted_prev_day = prev_day.strftime("%Y-%m-%d %H:%M:%S")
formatted_current_day = date_obj.strftime("%Y-%m-%d %H:%M:%S")
formatted_next_day = next_day.strftime("%Y-%m-%d %H:%M:%S")

# Printing the result in the required format
print(formatted_prev_day)
print(formatted_current_day)
print(formatted_next_day)