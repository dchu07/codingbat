def makes10(a, b):
    sum = a + b
    if sum == 10 or (a == 10 or b ==10):
        return True
    return False

#another solution
def makes10(a, b):
  return (a == 10 or b == 10 or a+b == 10)
