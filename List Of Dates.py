from datetime import datetime, timedelta

# Taking input from the user
date_str1 = input().strip()  # First date (e.g., 'Jul 11 2014')
date_str2 = input().strip()  # Second date (e.g., 'Jul 19 2014')

# Converting input dates to datetime objects
date1 = datetime.strptime(date_str1, "%b %d %Y")
date2 = datetime.strptime(date_str2, "%b %d %Y")

# Generating the list of dates between D1 and D2 (inclusive)
current_date = date1
while current_date <= date2:
    print(current_date.strftime("%Y-%m-%d %H:%M:%S"))
    current_date += timedelta(days=1)  # Move to the next day