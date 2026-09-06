def search(nums, target):
    """
    Binary Search
    Returns the index of target if found, otherwise -1.
    """
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
    """
    Fast Exponentiation
    Returns x raised to the power n.
    """
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


# ----- User Input -----

# Input for search()
nums = list(map(int, input("Enter sorted array elements: ").split()))
target = int(input("Enter target element: "))

index = search(nums, target)

if index != -1:
    print("Target found at index:", index)
else:
    print("Target not found.")


# Input for myPow()
x = float(input("\nEnter base: "))
n = int(input("Enter exponent: "))

result = myPow(x, n)

print("Computed value:", result)