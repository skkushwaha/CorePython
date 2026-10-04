person_details = {"name": "Jessa", "country": "USA", "telephone": 1178}
person_details.setdefault("state", "Texas")
person_details.setdefault("zip")
person_details.setdefault("country", "Canada")
print(person_details)

for key, value in person_details.items():
    print(key, ":", value)