from datetime import datetime, date, time, timedelta
td = date.today()
bd = date(year = 1990, month = 11, day = 14)
difference = td - bd
print("You were born", difference.days, "days ago.")
g_seconds = difference.total_seconds()
print("You have been alive for", int(g_seconds), "seconds.")
