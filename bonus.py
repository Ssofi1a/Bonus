time= input("Enter the time in format HH:MM:SS ")
hours, minutes, seconds = time.split(':')
hours = int(hours)
minutes = int(minutes)
seconds = int(seconds)

time_in_seconds = hours * 3600 + minutes * 60 + seconds

for i in range(time_in_seconds, 0, -1):
    minutes, seconds = divmod(i, 60)
    hours, minutes = divmod(minutes, 60)
    print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")

