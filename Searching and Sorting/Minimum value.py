def findMin(nums):
    left, right = 0, len(nums) - 1

    # If array is not rotated (first element < last element)
    if nums[left] < nums[right]:
        return nums[left]

    while left < right:
        mid = left + (right - left) // 2

        # If mid element is greater than rightmost element,
        # minimum must be in the right half
        if nums[mid] > nums[right]:
            left = mid + 1
        # If mid element is less than or equal to rightmost element,
        # minimum is in the left half (including mid)
        else:
            right = mid
    return nums[left]

# Example usage:
print(findMin([3, 4, 5, 1, 2]))