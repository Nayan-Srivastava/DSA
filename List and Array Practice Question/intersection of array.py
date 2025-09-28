def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))

# Example usage:
print(intersection([1, 2, 3], [4,5,6]))
print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))  #