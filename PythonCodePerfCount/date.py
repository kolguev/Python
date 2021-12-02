from datetime import timedelta, datetime, date, time

print(str(datetime.now() - timedelta(minutes=15))[:-3])