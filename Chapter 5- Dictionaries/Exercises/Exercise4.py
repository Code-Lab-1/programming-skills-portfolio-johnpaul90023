#A dictionary that includes three countries and its major rivers

rivers = {
    'Amazong': 'South America',
    'Yellow River': 'China',
    'Angara': 'Russia',
    }
print("")
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}. \n")

print("This collection of data includes the rivers listed below: \n")
for river in rivers.keys():
    print(f"- {river.title()} \n")

print("This collection of data includes the countries listed below: \n")
for country in rivers.values():
    print(f"- {country.title()} \n")