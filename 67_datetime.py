import datetime

today = datetime.date.today()
time_now = datetime.datetime.now()
time_now = time_now.strftime("%H:%M:%S %d-%m-%Y")

target_datetime = datetime.datetime(2030, 1, 2, 12, 30, 1)
current_catetime = datetime.datetime.now()

if target_datetime < current_catetime:
    print("Target date has passed.")
else:
    print("Target date has not passed.")
