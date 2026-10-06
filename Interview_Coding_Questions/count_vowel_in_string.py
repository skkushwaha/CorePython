def count_vowels(text):
    vowels = "aeiouAEIOU"
    count_vowels = 0
    for char in text:
        if char in vowels:
            count_vowels += 1
    return count_vowels

my_string = "shiv kumar kushwaha"
print(count_vowels(my_string))