from datetime import datetime as dt, timedelta as td

now = dt.now()
print("Current time: ", now)

future = now + td(days=7)
print("Time in a week: ", future)