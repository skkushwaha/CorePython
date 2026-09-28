# sorting a tuple that contains tuples as elements
# take employee tuple with id number, name, salary
emp = ((10, "Vijay", 9000.90), (20, "Nihaar", 5500.00), (30, "Vanaja", 8900.00), (40, "Kapoor", 5000.00))
print(sorted(emp))
print(sorted(emp, reverse=True))
print(sorted(emp, key=lambda x: x[1]))
print(sorted(emp, key=lambda x: x[2]))