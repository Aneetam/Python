from datetime import datetime, timedelta

def count_saturdays_sundays(D1, D2):
    # Convert input strings to datetime objects
    start_date = datetime.strptime(D1, "%d %b %Y")
    end_date = datetime.strptime(D2, "%d %b %Y")
    
    # Initialize counters
    saturday_count = 0  
    sunday_count = 0  

    # Iterate through all days from start_date to end_date
    current_date = start_date
    while current_date <= end_date:
        if current_date.weekday() == 5:  # Saturday
            saturday_count += 1
        elif current_date.weekday() == 6:  # Sunday
            sunday_count += 1
        current_date += timedelta(days=1)  # Move to next day
    
    # Print result in required format
    print(f"Saturday: {saturday_count}")
    print(f"Sunday: {sunday_count}")

# Take input
D1 = input().strip()
D2 = input().strip()

# Call function to count and print
count_saturdays_sundays(D1, D2)