import datetime

# datetime(year, month, day, hour, minute, second)
a = datetime.datetime(2022, 10, 14, 12, 30, 1)
b = datetime.datetime(2022, 10, 5, 22, 54, 1)

# returns a timedelta object
c = a - b
print('Difference: ', c)

minutes = c.total_seconds() / 60
print('Total difference in minutes: ', minutes)

# returns the difference of the time of the day
minutes = c.seconds / 60
print('Difference in minutes: ', minutes)