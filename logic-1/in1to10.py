def in1to10(n, outside_mode):
    if outside_mode and n <= 1 and 10 >= n:
        return True
    elif outside_mode and 1 < n < 10:
        return False
    elif outside_mode:
        return True
    elif 1 <= n <= 10:
        return True
    return False