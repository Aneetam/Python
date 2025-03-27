from datetime import datetime

# Taking UNIX timestamp as input
U = int(input().strip())

# Convert UNIX timestamp to a datetime object in UTC
utc_datetime = datetime.utcfromtimestamp(U)

# Format the datetime as "YYYY-MM-DD HH:MM:SS"
formatted_datetime = utc_datetime.strftime("%Y-%m-%d %H:%M:%S")

# Print the formatted datetime
print(formatted_datetime)