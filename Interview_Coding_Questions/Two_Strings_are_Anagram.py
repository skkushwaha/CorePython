def is_anagram(s, t):
    return sorted(s.lower()) == sorted(t.lower())
print(is_anagram("listen", "silent"))