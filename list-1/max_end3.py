def max_end3(nums):
    if nums[-1] > nums[0]:
        return [nums[-1], nums[-1], nums[-1]]
    elif nums[0] > nums[-1]:
        return [nums[0], nums[0], nums[0]]
    else:
        return [nums[0], nums[0], nums[0]]

#alternative solution
# def max_end3(nums):
#   big = max(nums[0], nums[2])
#   nums[0] = big
#   nums[1] = big
#   nums[2] = big
#   return nums