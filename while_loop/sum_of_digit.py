n = int(input("Please enter a number: "))
sum_of_digits = 0
while n > 0:
    r = n % 10
    sum_of_digits = sum_of_digits + r
    n = n // 10
print("The sum is", sum_of_digits)