import calendar

year = int(input("enter the year: "))
month = int(input("enter the month: "))
day = int(input("enter the day: "))
x = calendar.month(year, month, day)
print("the calender of the respective year and month_name: ", x)
