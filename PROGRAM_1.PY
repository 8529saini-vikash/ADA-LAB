def search(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def myPow(x, n):
    if n == 0:
        return 1.0

    if n < 0:
        x = 1 / x
        n = -n

    result = 1.0

    while n > 0:
        if n % 2 == 1:
            result *= x

        x *= x
        n //= 2

    return result

print(search([1, 3, 5, 7, 9, 11, 13], 7))
print(myPow(3, 5))
