def sum_of_elements(lst):
    total = 0
    for num in lst:
        total += num
    return total

# Example usage:
print(sum_of_elements([1, 2, 3, 4, 5]))  # Output: 15
print(sum_of_elements([-1, -2, -3, -4, -5])) # Output: -15