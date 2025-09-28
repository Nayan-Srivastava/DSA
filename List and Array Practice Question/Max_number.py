def find_max_element(lst):
    if len(lst) == 0:
        return None
    max_element = lst[0]
    for num in lst:
        if num > max_element:
            max_element = num
    return max_element
# Example usage:
print(find_max_element([3, 1, 4, 1, 5, 9, 2, 6, 5]))  # Output: 9
print(find_max_element([-7, -1, -3, -4]))  # Output: -1
print(find_max_element([]))  # Output: None