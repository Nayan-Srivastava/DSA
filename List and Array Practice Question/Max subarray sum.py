def max_subarray_sum(arr):
    if not arr:
        return 0

    max_ending_here = 0
    max_so_far = float('-inf')

    # Iterate through the array
    for x in arr:
        # Update max_ending_here to include current element
        max_ending_here = max(x, max_ending_here + x)
        # Update max_so_far to the maximum value found so far
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far