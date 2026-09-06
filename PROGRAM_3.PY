def findKthLargest(nums, k):
    """
    Returns the k-th largest element in the array.
    """
    sorted_nums = sorted(nums, reverse=True)
    return sorted_nums[k - 1]


def findMinMax(nums):
    """
    Returns the minimum and maximum elements as a tuple.
    """
    minimum = nums[0]
    maximum = nums[0]

    for num in nums[1:]:
        if num < minimum:
            minimum = num

        if num > maximum:
            maximum = num

    return minimum, maximum


# ----- User Input -----

nums = list(map(int, input("Enter unsorted array elements: ").split()))

k = int(input("Enter the value of k: "))

kth_largest = findKthLargest(nums, k)
minimum, maximum = findMinMax(nums)

print("Original array:", nums)
print(f"{k}th largest element:", kth_largest)
print("Minimum element:", minimum)
print("Maximum element:", maximum)
print("Min-Max pair:", (minimum, maximum))