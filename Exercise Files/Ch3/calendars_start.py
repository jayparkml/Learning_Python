#
# Example file for working with Calendars
#

# import the calendar module
import calendar

# create a plain text calendar
c = calendar.TextCalendar(calendar.SUNDAY) #MONDAY also possible
st = c.formatmonth(2017, 1, 0, 0)
print(st)

# create an HTML formatted calendar
hc = calendar.HTMLCalendar(calendar.SUNDAY)
st = hc.formatmonth(2017, 1)
print(st)

# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month


# for i in c.itermonthdays(2017,8):
#     print(i)
  

# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms

# for month in calendar.month_name:
#     print(month)

# for day in calendar.day_name:
#     print(day)

# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:
  
print("Team meetings will be on:")
for m in range(1, 13): # 13 is not inclusive
    cal = calendar.monthcalendar(2018, m)
    # print(cal)
    weekone = cal[0]
    weektwo = cal[1] #First friday should be within first 2 weeks

    if weekone[calendar.FRIDAY] != 0:
        meetday = weekone[calendar.FRIDAY]
    else:
        meetday = weektwo[calendar.FRIDAY]

    print("%10s %2d" % (calendar.month_name[m], meetday)) # %10s s:string 10: how many d: integer