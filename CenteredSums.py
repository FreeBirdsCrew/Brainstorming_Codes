def centered_average(nums):
    max = nums[0]
    min = nums[0]
    sum = nums[0]
    for i in range(1, len(nums)):
        sum += nums[i]
        if nums[i] > max:
            max = nums[i]
        elif nums[i] < min:
            min = nums[i]
    return (sum-max-min)/(len(nums)-2)


print(centered_average(([1, 2, 3, 4, 100])))
