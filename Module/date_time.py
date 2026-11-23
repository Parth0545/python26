import datetime
print(datetime.datetime.now())
print(datetime.datetime.now().time())
print(datetime.datetime.now().strftime("%H:%M:%S"))
print(datetime.date.today())
prev_time=datetime.datetime.now()
print(datetime.datetime.now()-datetime.timedelta(days=5))

