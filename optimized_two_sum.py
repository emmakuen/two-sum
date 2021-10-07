# Optimized version

def find_two_sum(nums, target):
    """Returns indexes of two integers in an array that sums up to target value"""
    target_hash = {}
    for i in range(len(nums)):
        if nums[i] in target_hash.keys():
            return [target_hash[nums[i]], i]
        else:
            target_hash[target - nums[i]] = i
    return


