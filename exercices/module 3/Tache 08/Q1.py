hour = int(input("Enter hour (0-23): "))

if hour == 0:
    print("12 AM")
elif hour < 12:
    print(hour, "AM")
elif hour == 12:
    print("12 PM")
else:

    Time = hour - 12
    print(Time, "PM")