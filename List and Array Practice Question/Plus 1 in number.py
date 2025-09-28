def plus_one(digits):
    n = len(digits)

    # Traverse the digits array from the last digit to the first
    for i in range(n - 1, -1, -1):
        # If the current digit is less than 9, simply increment it and return the array
        if digits[i] < 9:
            digits[i] += 1
            return digits
        # If the current digit is 9, set it to 0 and continue to the next digit
        digits[i] = 0

    # If all digits were 9, we need to add a new digit at the beginning
    return [1] + [0] * n

# Example usage:
print(plus_one([1, 2, 3]))  # Output: [1, 2, 4]
print(plus_one([9, 9, 9])) # Output: [1, 0, 0, 0]
print(plus_one([1,2,8])) # Output: [1, 3, 0]