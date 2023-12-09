from datetime import datetime, timedelta

def add_time(start, duration,starting_day=""):
    format = '%I:%M %p'
    #could be any date and time
    current_date = datetime.today()

    #change the current time to the input
    start_time = datetime.strptime(start, format)
    new_datetime = current_date.replace(hour=start_time.hour, minute=start_time.minute)
    
    #get the day of the week that is closest to the current time from the input,if given
    if starting_day !="":
        while str(new_datetime.strftime("%A")).lower() != starting_day.lower():
            new_datetime = new_datetime + timedelta(days=1)

    #add mathmatically the amount of minutes to the date
    duration = duration.split(":")
    minutes_val = int(duration[0])*60+int(duration[1])
    result = new_datetime + timedelta(minutes=minutes_val)
    
    #count days untill the dates are equall
    days_between = 0
    while result.date() !=new_datetime.date():
        new_datetime = new_datetime + timedelta(days=1)
        days_between+=1

    #the output that is required:
    if days_between == 0 and starting_day !="":#without starting day:
        return f'{result.strftime(format).lstrip("0")}, {result.strftime("%A")}'
    if days_between == 0 and starting_day =="":#with starting day:

        return f'{result.strftime(format).lstrip("0")}'
    if days_between == 1 and starting_day !="":#without starting day:
        return f'{result.strftime(format).lstrip("0")}, {result.strftime("%A")} (next day)'
    if days_between == 1 and starting_day =="":#with starting day:

        return f'{result.strftime(format).lstrip("0")} (next day)'
    if days_between > 1 and starting_day =="":#without starting day
        return f'{result.strftime(format).lstrip("0")} ({days_between} days later)'
    if days_between > 1 and starting_day !="":#with starting day
        return f'{result.strftime(format).lstrip("0")}, {result.strftime("%A")} ({days_between} days later)'
