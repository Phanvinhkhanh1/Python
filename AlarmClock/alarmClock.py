from datetime import datetime
from playsound import playsound

input_time = input("Please enter date by pattern (HH:MM:SS:PE) : ")

input_hour = input_time[0:2]
input_minute = input_time[3:5]
input_period = input_time[6:8].upper()

while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_period = now.strftime("%p")
    if current_period == input_period:
        if current_hour == input_hour:
            if current_minute == input_minute:
                # if current_second == input_second:
                    print("Wake up!")
                    playsound('alarm_tune.mp3')
                    break
