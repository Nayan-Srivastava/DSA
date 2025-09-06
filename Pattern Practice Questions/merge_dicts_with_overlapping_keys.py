def merge_dicts_with_overlapping_keys(dicts):
    merged_dict = {}
    for dict in dicts:
        for key, value in dict.items():
            merged_dict[key] = merged_dict.get(key, 0) + value
    return merged_dict


d=[{'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'c': 5, 'd': 6}]
print(merge_dicts_with_overlapping_keys(d))