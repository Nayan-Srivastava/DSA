def is_palindrome(lst):
    return lst == lst[::-1]

# Example usage:
print(is_palindrome([1, 2, 3, 2, 1]))  # Output: True
print(is_palindrome([1, 2, 3, 4, 5]))  # Output: False
print(is_palindrome(['a', 'b', 'c', 'b', 'a']))  # Output: True
print(is_palindrome(['a', 'b', 'c', 'd', 'e']))  # Output: False