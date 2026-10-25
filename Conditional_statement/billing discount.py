amount = int(input("Please enter your amount: "))
#TODO: Use an if-elif-else structure for discount logibelow
if amount < 1000:
    total = amount - amount * 0.10
elif amount >=1000 and amount <=5000:
    total = amount - amount * 0.15
elif amount > 5000 and amount < 1000:
    total = amount - amount * 0.20
else:
    total = amount - amount * 0.25

print('Pay:', total)