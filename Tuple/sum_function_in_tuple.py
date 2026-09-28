# program to find sum and average of element in a tuple
num = eval(input("Enter a number: "))
sum = 0
n = len(num)
for i in range(n):
    sum +=num[i]
print("Sum of numbers ",sum)
print("Average of numbers ",sum/n)