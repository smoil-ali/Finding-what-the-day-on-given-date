import calendar
date=list(map(int,input().split()))
val=calendar.weekday(date[2],date[0],date[1])
array=["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
print(array[val])