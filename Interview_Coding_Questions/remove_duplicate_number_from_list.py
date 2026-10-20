def remove_duplicate_numbers(nums):
    return list(dict.fromkeys(nums))
print(remove_duplicate_numbers([1, 3, 3, 54, 54, 55, 55]))

