def find_missing_number(nums):
    n = len(nums)
    total_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return total_sum - actual_sum

# Example usage:
print(find_missing_number([0, 1, 3]))  # Output: 2
print(find_missing_number([0, 1, 2, 4, 5]))  # Output: 3