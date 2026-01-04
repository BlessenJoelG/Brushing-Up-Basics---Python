import time
times = time.strftime('%H:%M:%S')
print(times)
timestamp = int(time.strftime('%H'))
if timestamp <12:
    print(f"Good Morning Sir, it's {times} in the morning")
elif timestamp >12 and timestamp < 16:
    print(f"Good afternoon Sir, it's {times} in the afternoon")
elif timestamp >16 and timestamp < 20:
    print(f"Good Evening Sir, it's {times} in the evening")
else:
    print(f"Good Night Sir, it's {times} in the night")