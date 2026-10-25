numbers = [12, 45, 7, 89, 23]  # You can change these values for testing

n = len(numbers)


i = 0

Min = 0
while i < n:
#
    if numbers[i] < Min:
        Min = numbers[i]
        i += 1

#TODO: Write the Logic to chack Max And Min using while loop below


print('Max Element:', Min)

