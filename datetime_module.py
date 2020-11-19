import datetime as dt

#  get the time in your timezone
now = dt.datetime.now()
year = now.month
print(now, year)


# set a date and time
my_birthday = dt.datetime(year=2000, month=12, day=1, hour=20)
print(my_birthday)

