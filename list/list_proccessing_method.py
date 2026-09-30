# python's list methods
num = [10, 20, 30, 40, 50]

n = len(num)
print("Number of elements in list: ", n)

num.append(60)
print("Num after appending 60", num)

num.insert(0, 5)
print("Number after inserting 5 at 0th position", num)

num1 = num.copy()
print('Newly created list num1: ', num1)
num.extend(num1)
print("Num after extending list: ", num)

n = num.count(50)
print("Number of elements in list: ", n)
num.remove(50)
print("Num after removing 50: ", num)
num.pop()
print("Num after removing ending element: ", num)
num.sort()
print("Num after sorting: ", num)
num.reverse()
print("Num after reversing: ", num)
num.clear()
print("Num after clearing: ", num)

