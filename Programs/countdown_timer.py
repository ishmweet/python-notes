import time

my_time = int(input("Enter the time in seconds: "))

for x in reversed(range(0, my_time)):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    days = int(x / 3600) % 24
    print(f"{days:02}:{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

time.sleep(0.5)

print("Time's up!")