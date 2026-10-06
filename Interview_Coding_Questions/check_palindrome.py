def is_palindrome(text):
    clean_text = text.lower()
    return clean_text == clean_text[::-1]

print(is_palindrome("abba"))