def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst

list_to_sort = [12, 11, 13, 5, 6]
sorted_list = insertion_sort(list_to_sort)
print("Sorted array is:", sorted_list)
