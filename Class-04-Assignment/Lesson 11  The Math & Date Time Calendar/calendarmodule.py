import calendar

# Check if a year is a leap year
print(calendar.isleap(2024))  # True

# Get the weekday of a specific date (0=Monday, 6=Sunday)
print(calendar.weekday(2023, 5, 15))  # Returns the weekday code

# Get a month's calendar as a string
print(calendar.month(2023, 5))
# Output:
#      May 2023
# Mo Tu We Th Fr Sa Su
#  1  2  3  4  5  6  7
#  8  9 10 11 12 13 14
# 15 16 17 18 19 20 21
# 22 23 24 25 26 27 28
# 29 30 31

# Get a year's calendar
print(calendar.calendar(2023))  # Prints entire year's calendar

# Get month range (weekday of first day, number of days)
print(calendar.monthrange(2023, 5))  # (0, 31) for May 2023