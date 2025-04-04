from datetime import datetime, date, timedelta

# Current date and time
now = datetime.now()
print(now)  # e.g., 2023-04-01 12:34:56.789012

# Specific date
d = date(2023, 4, 1)
print(d)    # 2023-04-01

# Date arithmetic
tomorrow = now + timedelta(days=1)
print(tomorrow)

# Formatting
print(now.strftime("%Y-%m-%d %H:%M:%S"))  # "2023-04-01 12:34:56"