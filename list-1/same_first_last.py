def same_first_last(nums):
    if len(nums) > 0 and nums[0] == nums[-1]:
        return True
    return False

#alternative solution
# def same_first_last(nums):
#   return (len(nums) >= 1 and nums[0] == nums[-1])
