num = int(input("Enter a number: "))
rev = 0
num_value = num
while num > 0:
    r = num % 10
    rev = rev * 10 + r
    num = num // 10
if rev == num_value:
    print("Number is Palindrome")
else:
    print("Number is not Palindrome")