n = int(input("Print number of elements: "))
i = 0
max_number = 0
while i < n:
    i = i + 1
    x= int(input(""))
    if x > max_number:
        max_number = x
print("Max number is: ",max_number)