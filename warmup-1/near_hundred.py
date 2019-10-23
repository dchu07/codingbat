def near_hundred(n):
  if abs(100-n) <= 10 or abs(200-n) <= 10:
    return True
  return False

#another solution
# def near_hundred(n):
#   return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))

