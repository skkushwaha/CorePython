list = []
print("How many elements ?", end=' ')
n = int(input())
for i in range(n):
    print("Enter the number: ", end=' ')
    list.append(int(input()))

largest = list[0]

for num in list:
    if num > largest:
        largest = num
print(largest)

# find smallest number
smallest = list[0]
for num in list:
    if num < smallest:
        smallest = num

print("Print smallest number in list: ",smallest)