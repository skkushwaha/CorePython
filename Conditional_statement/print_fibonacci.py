num = int(input("Please enter a number: "))
a, b = 0, 1
count = 0
print("Fibonacci sequence")
while count < num:
    print(a, end='')
    a, b = b, a+b
    count += 1