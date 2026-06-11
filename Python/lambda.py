people = [
    {"name": "Aegon", "house": "Targaryen"},
    {"name": "Brandon", "house": "Stark"},
    {"name": "Tyrion", "house": "Lannister"},
    {"name": "Robert", "house":"Baratheon"},
    {"name": "Jaime", "house": "Lannister"},
    {"name": "Rob", "house": "Stark"}
]

# people.sort()
# print(people) # TypeError

def f(person):
    return person["name"]

people.sort(key=f)
print(people) # [{'name': 'Aegon', 'house': 'Targaryen'}, {'name': 'Brandon', 'house': 'Stark'}, {'name': 'Jaime', 'house': 'Lannister'}, {'name': 'Rob', 'house': 'Stark'}, {'name': 'Robert', 'house': 'Baratheon'}, {'name': 'Tyrion', 'house': 'Lannister'}]

# Sorting using "lambda" function

people.sort(key=lambda person: person["name"])
print(people) # [{'name': 'Aegon', 'house': 'Targaryen'}, {'name': 'Brandon', 'house': 'Stark'}, {'name': 'Jaime', 'house': 'Lannister'}, {'name': 'Rob', 'house': 'Stark'}, {'name': 'Robert', 'house': 'Baratheon'}, {'name': 'Tyrion', 'house': 'Lannister'}]
