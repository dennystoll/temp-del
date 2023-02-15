import datetime, time 

time = datetime.datetime.now()

current_minute = time.strftime("%M")

current_minute = int(current_minute)

opt_min_1 = 30

opt_min_2 = 60

mins_left= 0

def countdown():
    if current_minute <= opt_min_1:
        mins_left = opt_min_1 - current_minute
    elif current_minute > opt_min_1:
        mins_left = opt_min_2 - current_minute
    else:
        print("Something went wrong...")
    return mins_left