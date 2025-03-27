from datetime import datetime

def time_until_new_year(D):
    # Convert input string to datetime object
    current_datetime = datetime.strptime(D, "%b %d %Y %I:%M %p")

    # Get the next year's January 1st at 00:00 AM
    new_year_datetime = datetime(year=current_datetime.year + 1, month=1, day=1, hour=0, minute=0)

    # Calculate the time difference
    time_remaining = new_year_datetime - current_datetime
    total_minutes = time_remaining.total_seconds() // 60  # Convert to minutes

    # Extract hours and minutes
    hours = int(total_minutes // 60)
    minutes = int(total_minutes % 60)

    # Print result
    print(f"{hours} hours {minutes} minutes")

# Take input
D = input().strip()

# Call function
time_until_new_year(D)