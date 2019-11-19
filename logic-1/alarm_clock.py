def alarm_clock(day, vacation):
    if vacation and 1 <= day <= 5:
        return "10:00"
    elif vacation:
        return "off"
    elif day == 0 or day == 6:
        return "10:00"
    else:
        return "7:00"