
# Datetime

# a date in python is not a data type of its own, but we can import a module named datatime
# to work with dates as date objects.

import datetime
x = datetime.datetime.now()
print(x)

# The date contains year, months, day, hour, minutes, second, and millisecond.
# The datetime module has many methods to return information about the date object.

print(x.strftime("%A")) # return the year and name of weekday:

# Creating Date object
# to create a date, we can use the datetime() class (constructor) of the datetime module.
# to datetime() class requires the three parameters to create a date: year, month, day.

y = datetime.datetime(2020, 2, 6)
print(y)

# The datetime() class also takes parameters for time and timezone
# (hour, minute, second, microsecond, tzone), but they are optional,
# and has a default value of 0, (None for timezone).

# The srttime() method
# the datetime objects has a method for formatting date objects into readable strings.
# the method is called strftime(), and takes one parameter, format, to specify the
# format of the returned string:

print(x.strftime("%B"))


# HACK: a reference of all the legal format codes:

# %a	Weekday, short version	Wed
# %A	Weekday, full version	Wednesday
# %w	Weekday as a number 0-6, 0 is Sunday	3
# %d	Day of month 01-31	31
# %b	Month name, short version	Dec
# %B	Month name, full version	December
# %m	Month as a number 01-12	12
# %y	Year, short version, without century	18
# %Y	Year, full version	2018
# %H	Hour 00-23	17
# %I	Hour 00-12	05
# %p	AM/PM	PM
# %M	Minute 00-59	41
# %S	Second 00-59	08
# %f	Microsecond 000000-999999	548513
# %z	UTC offset	+0100
# %Z	Timezone	CST
# %j	Day number of year 001-366	365
# %U	Week number of year, Sunday as the first day of week, 00-53	52
# %W	Week number of year, Monday as the first day of week, 00-53	52
# %c	Local version of date and time	Mon Dec 31 17:41:00 2018
# %C	Century	20
# %x	Local version of date	12/31/18
# %X	Local version of time	17:41:00
# %%	A % character	%
# %G	ISO 8601 year	2018
# %u	ISO 8601 weekday (1-7)	1
# %V	ISO 8601 weeknumber (01-53)	01
