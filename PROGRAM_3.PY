def findKthLargest(nums, k):
    sorted_nums = sorted(nums, reverse=True)
    return sorted_nums[k - 1]


def findMinMax(nums):
    minimum = nums[0]
    maximum = nums[0]

    for num in nums[1:]:
        if num < minimum:
            minimum = num

        if num > maximum:
            maximum = num

    return minimum, maximum


nums = [23, 54, 67, 89, 63, 12, 75, 34]

print(findKthLargest(nums, 4))
print(findMinMax(nums))