def big_diff(nums):
    max = nums[0]
    min = nums[0]
    for i in range(0,len(nums)-1):
        if nums[i] > max:
            max = nums[i]
        elif nums[i] < min:
            min = nums[i]
    return(max-min)

print(big_diff([10, 3, 5, 6]))
