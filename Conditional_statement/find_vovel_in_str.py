text = input("Please enter text with vovel: ")
vovel = "aeiouAEIOU"
vovel_count = 0
for char in text:
    if char in vovel:
        vovel_count += 1
print(vovel_count)

