def searchRange(nums, target):
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            left, right = mid, mid
            while left >= start and nums[left] == target:
                left -= 1
            while right <= end and nums[right] == target:
                right += 1
            return [left + 1, right - 1]
        if nums[mid] < target:
            start = mid + 1
        elif nums[mid] > target:
            end = mid - 1
    return [-1, -1]

# Example usage:
print(searchRange([5, 7, 7, 8, 8, 10], 8))  # Output: [3, 4]
