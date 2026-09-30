# creating list using range function
list1 = range(10)
for i in list1:
    print(i, ",", end='')
print()

list2 = range(5, 10)
for i in list2:
    print(i, ",", end='')
print()

list3 = range(5, 10, 2)
for i in list3:
    print(i, ",", end='')
print()
# while list to access elements from a list
i = 0
while i < (len(list1)):
    print(list1[i], ",", end='')
    i += 1
