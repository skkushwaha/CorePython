def fib_num(n):
    a, b = 0, 1
    for i in range(n+1):
        yield a
        a, b = b, a+b
num = int(input("Enter a number: "))
for term in fib_num(num):
    print(term, end=" ")
