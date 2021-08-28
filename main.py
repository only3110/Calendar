#program to make calendar
#import package
import calendar

#year and month input
yy = int(input("Year: "))
mm = int(input("Month: "))

#print the calendar
print(calendar.month(yy, mm))