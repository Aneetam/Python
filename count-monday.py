from datetime import datetime
A,B=map(int,input().split())
count=0
for year in range(A,B+1):
    for month in range(1,13):
        first_day=datetime(year,month,1)
        if first_day.strftime("%A") =="Monday":
            count+=1
            
print(count)