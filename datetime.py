#This program calculates the total number of seconds the user has been alive.

from datetime import datetime, date, time, timedelta
td = date.today()
bd = date(year = 1991, month = 1, day = 2)
difference = td - bd
print("You were born", difference.days, "days ago.")
t_seconds = difference.total_seconds()
print("You have been alive for", int(t_seconds), "seconds.")
