# inserting element s from keyboard and find element position
str = input("Enter elements separated by command : " ).split(',')

lst = [int(num) for num in str]
tup = tuple(lst)
print(tup)
ele = int(input("Enter element to find position : "))
try:
    pos = tup.index(ele)
    print("Print element at position ",pos+1)
except ValueError:
    print("Element is not present in the tuple")