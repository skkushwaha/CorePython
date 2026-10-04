person_details = {"name": "Jessa", "country": "USA", "telephone": 1178, "age": 25, "weight" : 52}
deleted_item = person_details.popitem()
print(deleted_item)
print(person_details)

deleted_item = person_details.pop("name")
print(deleted_item)
print(person_details)
print(deleted_item)
del person_details["country"]
print(person_details)