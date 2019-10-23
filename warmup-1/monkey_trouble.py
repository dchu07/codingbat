def monkey_trouble(a_smile, b_smile):
    if a_smile == True and b_smile == True:
        return True
    elif a_smile == False and b_smile == False:
        return True
    return False



#another solution
# def monkey_trouble(a_smile, b_smile):
#     if a_smile and b_smile:
#         return True
#     elif not a_smile and not b_smile:
#         return True
#     return False