from datetime import datetime

date_str = input()
date_obj = datetime.strptime(date_str, "%d %b %Y")
formatted_date = date_obj.strftime("%Y-%m-%d %H:%M:%S")
print(date_obj)
print("Formatted Date:", formatted_date)