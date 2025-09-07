import datetime #biblioteka za vreem

date = datetime.date(2025,1,1)
print(date)
today = date.today()
print(today)
time = datetime.time(12,24,30)
print(time)
now = datetime.datetime.now()
print(now.strftime("%H:%M:%S"))