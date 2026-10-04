# counting how many times an element occurred in the list
x = []
n = int(input("How many elements do you want?"))
for i in range(n):
    print("Please enter the element", end='')
    element = int(input())
    x.append(element)
print("The list is: ", x)
y = int(input("Enter elements to count: "))
c = 0
for i in x:
    if (y==i):
        c = c+1
print(f'{y} is found {c} times in the list')
