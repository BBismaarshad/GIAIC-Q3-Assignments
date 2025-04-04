from datetime import datetime, date, time, timedelta

# Current date and time
now = datetime.now()
print(now)  # e.g., 2023-05-15 14:30:45.123456

# Creating specific dates
d = date(2023, 5, 15)
print(d)  # 2023-05-15

# Creating specific times
t = time(14, 30, 45)
print(t)  # 14:30:45

# Formatting dates
formatted = now.strftime("%d-%m-%Y %H:%M:%S")
print(formatted)  # e.g., "15-05-2023 14:30:45"

# Parsing dates from strings
date_str = "15 May 2023"
parsed = datetime.strptime(date_str, "%d %B %Y")
print(parsed)  # 2023-05-15 00:00:00

# Date arithmetic
future = now + timedelta(days=7)
print(future)  # 7 days from now

difference = future - now
print(difference.days)  # 7