def love6(a,b):
    if a + b == 6:
        return True
    elif a - b == 6 or b - a == 6:
        return True
    elif a == 6 or b == 6:
        return True
    return False