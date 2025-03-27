from datetime import datetime
date_str=input().strip()
date_obj=datetime.strptime(date_str,"%d %b %Y")
day_name=date_obj.strftime("%A")
print(day_name)Name of weekday