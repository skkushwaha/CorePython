def find_largest_number(numbers):
    # check empty list
    if not numbers:
        return None
    largest = numbers[0]
    for num in numbers:
       if num > largest:
           largest = num
    return largest

print(find_largest_number([1, 2, 34, 4, 5]))
