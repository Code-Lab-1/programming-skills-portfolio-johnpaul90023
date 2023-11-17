#Each time the pets are added to the empty list of pets, their data is stored.

pets = []
pet = {
    'animal type': 'lion',
    'owner': 'jeff',
    'name': 'owen',
    'weight': 193,
    'eats': 'dears',
}
pets.append(pet)

pet = {
    'animal type': 'hamster',
    'owner': 'paul',
    'name': 'dave',
    'weight': 12,
    'eats': 'seeds',
}
pets.append(pet)

pet = {
    'animal type': 'turtle',
    'owner': 'jefferson',
    'name': 'mack',
    'weight': 112,
    'eats': 'seaweed',
}
pets.append(pet)

for pet in pets:
    print(f"\nListed below are the datas of {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"{key}: {value}")