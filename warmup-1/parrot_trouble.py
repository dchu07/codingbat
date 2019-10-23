def parrot_trouble(talking, hour):
    if talking and (hour < 7 or 20 < hour <= 23):
        return True
    return False

#another solution
# def parrot_trouble(talking, hour):
#     return (talking and (hour < 7 or hour > 20))