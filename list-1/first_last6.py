def first_last6(nums):
    if nums[0] == 6 or nums[-1] == 6:
        return True
    return False

#alternative solution
# def first_last6(nums):
#   return (nums[0]==6 or nums[-1]== 6)